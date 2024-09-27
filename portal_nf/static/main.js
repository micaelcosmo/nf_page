// Experimental Class
document.addEventListener("DOMContentLoaded", function() {
    const experimentalClassesManagementButton = document.getElementById('experimental-classes-management-button');
    const experimentalClassButton = document.getElementById('request-experimental-class-button');
    if (experimentalClassesManagementButton) {
        experimentalClassesManagementButton.addEventListener('click', () => {
            window.location.href = 'experimental_classes_management/';
        });
    } else if (experimentalClassButton) {
        experimentalClassButton.addEventListener('click', () => {
            window.location.href = 'request_experimental_class/';
        });
    } else {
        console.error("Elemento com ID de 'experimentalClass ou experimentalClasses' não encontrado.");
    }
});

// Register
document.getElementById('register-button').addEventListener('click', function() {
    window.location.href = 'register/';
  });

// Login
document.getElementById('login-button').addEventListener('click', function() {
    window.location.href = 'login/';
});

// Classes Schedules
document.getElementById('class-schedules-button').addEventListener('click', function() {
    window.location.href = 'class_schedules/';
});
// Classes Schedules - Management
document.getElementById('manage-class-schedules-button').addEventListener('click', function() {
    window.location.href = 'manage_class_schedules/';
});

// Nav Bar
function toggleMenu() {
    const menu = document.querySelector('.navbar .menu');
    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
}