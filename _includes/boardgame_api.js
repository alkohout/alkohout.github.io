
// Shared auth + fetch helpers, loaded by every page. The token is issued at
// login and sent on every call; a 401 means it has expired or been revoked,
// so the page clears it and goes back to the login screen rather than
// rendering an empty dashboard.

function getToken() {
    return localStorage.getItem('bg_token');
}

function requireAuth() {
    if (!getToken()) {
        window.location.href = './index.html';
        throw new Error('Not authenticated');
    }
}

async function apiFetch(path, options = {}) {
    const token = getToken();
    const headers = { 'Content-Type': 'application/json', ...(options.headers || {}) };
    if (token) headers['Authorization'] = 'Bearer ' + token;

    const resp = await fetch(API_BASE + path, { ...options, headers });

    if (resp.status === 401) {
        localStorage.removeItem('bg_token');
        window.location.href = './index.html';
        return null;
    }
    return resp;
}

// Fetch an image the same way as everything else — with a bearer token — and
// hand back a blob URL. An <img src> can't carry an Authorization header, and
// making photos publicly addressable would undo the isolation everything else
// has.
const _blobCache = new Map();

async function apiImageUrl(path) {
    if (_blobCache.has(path)) return _blobCache.get(path);
    const r = await apiFetch(path);
    if (!r || !r.ok) return null;
    const url = URL.createObjectURL(await r.blob());
    _blobCache.set(path, url);
    return url;
}

// Shrink a photo before it leaves the phone. A modern camera shot is 3-5 MB
// of detail nobody needs to see the state of a board, and uploading it over a
// mobile connection is the slow part.
const PHOTO_MAX_EDGE = 1600;

function shrinkImage(file, maxEdge = PHOTO_MAX_EDGE, quality = 0.82) {
    return new Promise(resolve => {
        const img = new Image();
        img.onload = () => {
            const scale = Math.min(1, maxEdge / Math.max(img.width, img.height));
            // Already small enough: don't re-encode and lose quality for nothing.
            if (scale === 1 && file.size <= 900 * 1024) { resolve(file); return; }
            const canvas = document.createElement('canvas');
            canvas.width = Math.round(img.width * scale);
            canvas.height = Math.round(img.height * scale);
            canvas.getContext('2d').drawImage(img, 0, 0, canvas.width, canvas.height);
            canvas.toBlob(
                blob => resolve(blob
                    ? new File([blob], 'photo.jpg', { type: 'image/jpeg' })
                    : file),
                'image/jpeg', quality);
        };
        img.onerror = () => resolve(file);   // not decodable here; let the server judge
        img.src = URL.createObjectURL(file);
    });
}
