<template>
    <div class="container">
      <h1>Movies Collection</h1>
      <div v-if="movies.length === 0" class="no-movies">No movies available to show</div>
      <div v-else class="movies-grid">
        <div v-for="movie in movies" :key="movie.id" class="movie-item">
            <div class="movie-content">
            <img :src="getPoster(movie.poster)" :alt="movie.title" class="movie-image" />
          <div class="movie-info">
            <h3 class="movie-title">{{ movie.title }}</h3>
            <p class="movie-description">{{ movie.description }}</p>
          </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const movies = ref([]);
  
  async function fetchMovies() {
    try {
      const response = await fetch('/api/v1/movies');
      if (response.ok) {
        const data = await response.json();
        movies.value = data.movies;
      } else {
        console.error('Failed to fetch movies');
      }
    } catch (error) {
      console.error('Error fetching movies:', error);
    }
  }
  function getPoster(filename){
    return `/api/v1/posters/${filename}`
  }


  onMounted(() => {
    fetchMovies();
  });
  </script>
  
  <style scoped>
  .container {
    max-width: 1260px;
    margin: 0 auto;
    padding: 10px;
  }
  h1{
    margin-left:0px;
    margin-bottom: 15px;
  }
  .movies-grid {
    display: grid;
    grid-template-columns:repeat(2, minmax(200px, 1fr));
    grid-gap: 30px;
  }
  
  .movie-item {
    background-color: #f1f1f1;
    border-radius: 4px;
    overflow: hidden;
    transition: transform 0.3s ease;
  }
  
  .movie-item:hover {
    transform: scale(1.05);
  }
  .movie-content{
    display: flex;
  }
  
  .movie-image {
    width: 100%;
    height: 400px;
    object-fit: cover;
  }
  
  .movie-info {
    padding: 15px;
  }
  
  .movie-title {
    margin-top: 0;
    margin-bottom: 5px;
    font-size: 1.2rem;
  }
  
  .movie-description {
    margin: 0;
    font-size: 0.9rem;
    color: #666;
  }
  
  .no-movies {
    text-align: center;
    font-size: 1.2rem;
    color: #888;
    margin-top: 40px;
  }
  </style>