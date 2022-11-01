import { applicationDefault, initializeApp } from 'firebase-admin/app';
import { getStorage } from 'firebase-admin/storage';
export { Storage } from '@google-cloud/storage';

const app = initializeApp({
    credential: applicationDefault(),
    storageBucket: 'blog-8317b.appspot.com'
})

export const storageBucket = getStorage(app).bucket()
