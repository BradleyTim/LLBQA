// let version = 1;
// let cacheName = `cache-v${version}`;
// let dataCacheName = `LLBQA-v${version}`;
// const cacheAssetFiles = [
//   '/static/css/admin.css',
//   '/static/css/main.css',
//   '/static/css/bootstrap.css',
//   '/static/js/main.js',
//   '/static/manifest.json',
//   '/static/favicon.ico',
//   '/static/images/icons/icon-192x192.png',
//   '/static/images/icons/icon-384x384.png',
//   '/static/images/icons/icon-512x512.png',
// ];

// self.addEventListener('install', (e) => {
//   console.log('serviceWorker installed!!!');
//   self.skipWaiting();

//   e.waitUntil(
//     caches.open(cacheName)
//       .then(cache => {
//         console.log('caching files...');
//         return cache.addAll(cacheAssetFiles);
//       })
//   );
// });


// self.addEventListener('activate', (e) => {
//   console.log('serviceWorker activated!!!');

//   e.waitUntil(
//     caches.keys()
//       .then(cacheNames => {
//         return Promise.all(cacheNames.map(thisCacheName => {
//           if (thisCacheName !== cacheName && thisCacheName !== dataCacheName) {
//             console.log('serviceWorker deleting outdated cache');
//             return caches.delete(thisCacheName);
//           }
//         }))
//       })
//   );
// });


// self.addEventListener('fetch', (e) => {
//   console.log('serviceWorker request for ', e.request.url);

//   const req = e.request;
//   const dataUrl = new URL(req.url);

//   if (dataUrl.origin === location.origin) {
//     e.respondWith(cacheFirst(req));
//   } else {
//     e.respondWith(networkFirst(req));
//   }

// });

// async function cacheFirst(req) {
//   const cacheResponse = await caches.match(req);
//   return cacheResponse || fetch(req);
// }

// async function networkFirst(req) {
//   const cache = await caches.open(dataCacheName);

//   try {
//     const response = await fetch(req);
//     cache.put(req, response.clone());
//     return response;
//   } catch (error) {
//     const cachedResponse = await cache.match(req);
//     return cachedResponse || caches.match('/offline.json');
//   }

// }