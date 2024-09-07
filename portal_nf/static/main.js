
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
    