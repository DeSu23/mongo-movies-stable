window.onload = async function () {
    const movieContainer = document.getElementById('movie-container');
    const movieId = window.location.pathname.split('/')[2];

    try {
        const embedUrl = `https://vidsrc.to/embed/movie/${movieId}`;
        const iframe = document.createElement('iframe');
        iframe.src = embedUrl;
        iframe.style.width = '100vw';
        iframe.style.height = '100vh';
        movieContainer.style.display = 'flex';
        movieContainer.style.justifyContent = 'center';
        movieContainer.style.alignItems = 'center';

        iframe.frameBorder = '0';
        iframe.referrerPolicy = 'origin';
        iframe.allowFullscreen = true;

        movieContainer.appendChild(iframe);
    } catch (error) {
        console.error('Error fetching movie:', error);
    }
};
