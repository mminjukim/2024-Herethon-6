document.querySelector('.comment-input button').addEventListener('click', function() {
    const commentText = document.querySelector('.comment-input input').value;
    if (commentText.trim() !== '') {
        const commentSection = document.querySelector('.comments');
        
        const newComment = document.createElement('div');
        newComment.classList.add('comment');
        
        const userImage = document.createElement('img');
        userImage.src = 'images/comment_user_default.png';
        userImage.alt = 'User';
        
        const commentContent = document.createElement('div');
        commentContent.classList.add('comment-content');
        
        const userName = document.createElement('span');
        userName.textContent = '새로운 사용자';
        
        const commentTextElement = document.createElement('p');
        commentTextElement.textContent = commentText;
        
        commentContent.appendChild(userName);
        commentContent.appendChild(commentTextElement);
        
        newComment.appendChild(userImage);
        newComment.appendChild(commentContent);
        
        commentSection.appendChild(newComment);
        
        document.querySelector('.comment-input input').value = '';
    }
});
