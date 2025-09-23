document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');

    if (!menuToggle || !mobileMenu) {
        console.error('Menu elements not found at 2:34 PM WAT, Sep 22, 2025:', { menuToggle, mobileMenu });
        return;
    }
    console.log('Menu elements found and ready at 2:34 PM WAT, Sep 22, 2025');

    menuToggle.addEventListener('click', () => {
        console.log('Menu toggle clicked at 2:34 PM WAT, Sep 22, 2025');
        mobileMenu.classList.toggle('hidden');
    });
});