from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Posted
from .forms import PostForm


# list shob posts dekhao

def post_list(request):
    posts=Posted.objects.filter(status='published')
    #filter() diya sudhu published posts nichi
    return render(request,'blog/post_list.html',{'posts':posts})


#Detail ekta post dekhao
def post_detail(request,pk):
    post=get_object_or_404(Posted,pk=pk)
    #pk na pale 404 page dekhabe, crash korbe na
    return render(request,'blog/post_detail.html',{'post':post})


#create new post
@login_required #login na thakle/accounts/login/e jabe
def post_create(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False) #DB te save koro na ekhono
            post.author=request.user     #author set koro
            post.save()                  #ekhono save koro

            post.tags.set(form.cleaned_data['tags']) #M2M save
            return redirect('blog:post-detail',pk=post.pk)
        
    else:
        form=PostForm()
    return render(request,'blog/post_form.html',{'form':form,'action':'Create'})


# post edit kora
@login_required
def post_edit(request,pk):
    post=get_object_or_404(Posted,pk=pk)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post) #instance dile update hoy
        if form.is_valid():
            form.save()
            return redirect('blog:post-detail',pk=post.pk)
    else:
        form=PostForm(instance=post)  #form pre-fill hobe
    return render(request,'blog/post_form.html',{'form':form,'action':'Edit'})


#Delete post
@login_required
def post_delete(request,pk):
    post=get_object_or_404(Posted,pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog:post-list')
    return render(request,'blog/post_confirm_delete.html',{'post':post})
