<template>
  <div>
    <h1>Все изображения</h1>
    <div class="all-images">
      <div v-for="image in images" :key="image">
        <img :src="'http://localhost:5000/uploads/' + image" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      images: []
    };
  },
  async mounted() {
    const response = await axios.get("http://localhost:5000/images");
    this.images = Object.values(response.data).flat();
  }
};
</script>

<style scoped>
.all-images {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

img {
  width: 150px;
  height: auto;
}
</style>
