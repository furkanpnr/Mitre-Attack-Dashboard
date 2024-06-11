document.addEventListener("DOMContentLoaded", function() {
    var path = window.location.pathname;
    var sidebarItems = document.querySelectorAll('.sidebar-list-item a');
    sidebarItems.forEach(function(item) {
        if (item.getAttribute('href') === path) {
            item.parentElement.classList.add('active');
        }
    });
});


function setTheme(theme) {
    document.cookie = `theme=${theme};path=/;max-age=31536000`; 
    document.documentElement.className = theme;
}


window.onload = function() {
    const cookies = document.cookie.split('; ').reduce((acc, cookie) => {
        const [key, value] = cookie.split('=');
        acc[key] = value;
        return acc;
    }, {});
    
    const theme = cookies.theme || 'dark';
    document.documentElement.className = theme;
    
    if (theme === 'light') {
        modeSwitch.classList.add('active');
    } else {
        modeSwitch.classList.remove('active');
    }
}

var modeSwitch = document.querySelector('.mode-switch');
modeSwitch.addEventListener('click', function () {                     
    const currentTheme = document.documentElement.className;
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    modeSwitch.classList.toggle('active');
});


