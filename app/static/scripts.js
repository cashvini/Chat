let menu = document.querySelector('#menu-icon');
let navlist =  document.querySelector('.navlist');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navlist.classList.toggle('open');

    console.log(navlist);
};

const sr = ScrollReveal ({
    distance: '65px',
    duration: 2600,
    delay: 450,
    reset: true
});

sr.reveal('.hero-text',{delay:200, origin:'top'});
sr.reveal('.hero-img',{delay:450, origin:'top'});
sr.reveal('.icons',{delay:500, origin:'top'});
sr.reveal('.scroll-down',{delay:500, origin:'top'});



document.getElementById("signup-modal").style.display = 'none'; 
function closeLoginModal() {
    document.getElementById("login-modal").style.display = 'none';
    document.getElementById("signup-modal").style.display = 'block';  
    document.getElementById("modal_title_Login").style.display = 'none';    
    document.getElementById("modal_title_Signup").style.display = 'block'; 
}
function closeSignupModal() {
    document.getElementById("login-modal").style.display = 'block';
    document.getElementById("signup-modal").style.display = 'none';   
    document.getElementById("modal_title_Signup").style.display = 'none';
    document.getElementById("modal_title_Login").style.display = 'block';    
}