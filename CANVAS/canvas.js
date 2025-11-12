// Interactividad para el Canvas Personal
document.addEventListener('DOMContentLoaded', function() {
    const canvasSections = document.querySelectorAll('.canvas-section');
    
    canvasSections.forEach(section => {
        section.addEventListener('mouseenter', function() {
            this.style.borderColor = '#00ffff';
            this.style.boxShadow = '0 0 20px rgba(0,255,255,0.3)';
        });
        
        section.addEventListener('mouseleave', function() {
            this.style.borderColor = 'rgba(255,255,255,0.2)';
            this.style.boxShadow = 'none';
        });
        
        section.addEventListener('click', function() {
            this.classList.toggle('expanded');
        });
    });

    // Efecto de video placeholder
    const videoButtons = document.querySelectorAll('.cyber-button');
    videoButtons.forEach(button => {
        button.addEventListener('click', function() {
            const placeholder = this.closest('.video-placeholder');
            placeholder.innerHTML = `
                <div class="video-playing">
                    <p>🎬 Video reproduciéndose...</p>
                    <div class="video-progress">
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 0%"></div>
                        </div>
                    </div>
                    <button class="cyber-button" onclick="this.closest('.video-playing').innerHTML='🎥 Video finalizado'">DETENER</button>
                </div>
            `;
            
            // Simular progreso de video
            const progressFill = placeholder.querySelector('.progress-fill');
            let progress = 0;
            const interval = setInterval(() => {
                progress += 2;
                progressFill.style.width = progress + '%';
                if (progress >= 100) {
                    clearInterval(interval);
                }
            }, 100);
        });
    });
});