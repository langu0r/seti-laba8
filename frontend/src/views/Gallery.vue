<template>
    <div class="gallery">
      <h1>Фото-галерея</h1>
      <div v-if="selectedImage">
        <h3>Выбранное изображение: {{ selectedImage }}</h3>
        <img :src="'http://localhost:5000/uploads/' + selectedImage" v-if="selectedImage" class="selected-img" />
      </div>
  
      <div>
        <button @click="fetchImages">Загрузить изображения</button>
        <button @click="viewAll">Все на одной странице</button>
      </div>
  
      <div class="images">
        <div v-for="image in images" :key="image">
          <img :src="'http://localhost:5000/uploads/' + image" @click="selectImage(image)" />
        </div>
      </div>
  
      <form @submit.prevent="uploadImage">
        <input type="file" ref="fileInput" />
        <button type="submit">Загрузить</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        images: [],
        selectedImage: null
      };
    },
    methods: {
      async fetchImages() {
        const response = await axios.get("http://localhost:5000/images");
        this.images = Object.values(response.data).flat();
      },
      async selectImage(image) {
        this.selectedImage = image;
        await axios.post("http://localhost:5000/select", { filename: image });
      },
      async uploadImage() {
        const file = this.$refs.fileInput.files[0];
        if (!file) return;
  
        const formData = new FormData();
        formData.append("file", file);
  
        await axios.post("http://localhost:5000/upload", formData);
        this.fetchImages();
      },
      viewAll() {
        this.$router.push("/all");
      }
    },
    async mounted() {
      const response = await axios.get("http://localhost:5000/selected");
      this.selectedImage = response.data.filename;
      this.fetchImages();
    }
  };
  </script>
  
  <style scoped>
  .images {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  
  img {
    width: 100px;
    height: auto;
    cursor: pointer;
  }
  
  .selected-img {
    width: 300px;
    height: auto;
    margin-top: 10px;
  }
  </style>
  