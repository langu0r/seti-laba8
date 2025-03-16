import { createRouter, createWebHistory } from 'vue-router';
import Gallery from '@/views/Gallery.vue';
import AllImages from '@/views/AllImages.vue';

const routes = [
  {
    path: '/',
    name: 'Gallery',
    component: Gallery
  },
  {
    path: '/all',
    name: 'AllImages',
    component: AllImages
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
