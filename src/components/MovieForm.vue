<template>
    <form id="movieForm" @submit.prevent="saveMovie">
      <div v-if="showSuccessMessage" class="alert alert-success mt-3">
        {{ successMessage }}
      </div>

      <div v-if="showErrorMessages" class="alert alert-danger mt-3">
        <ul>
          <li v-for="error in errorMessages" :key="error">{{ error }}</li>
        </ul>
      </div>

      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" v-model="formData.title" name="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea v-model="formData.description" name="description" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input type="file" @change="handleFileUpload" class="form-control" />
      </div>

      <button type="submit" class="btn btn-primary">Save Movie</button>
    </form>
  </template>


<script setup>
import { ref, onMounted } from 'vue';

let csrfToken = ref('');
let showSuccessMessage = ref(false);
let showErrorMessages = ref(false);
let successMessage = ref("");
let errorMessages = ref([]);

let formData = ref({
  title: '',
  description: '',
  poster: '',
});

function handleFileUpload(event) {
  formData.poster = event.target.files[0];
}

async function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  form_data.append("poster", formData.poster);
  
  try{
    const response = await fetch("/api/v1/movies", {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrfToken.value
      },
    });
    
    if (response.ok) {
        const data = await response.json();
        showSuccessMessage.value = true;
        showErrorMessages.value = false;
        successMessage.value = data.message;
        clearFormData();

      } else {
        const errorData = await response.json();
        showSuccessMessage.value = false;
        showErrorMessages.value = true;
        errorMessages.value = errorData.errors;
      }
  } catch (error) {
    console.error("Error in saving Movie:", error);
    showSuccessMessage.value = false;
    showErrorMessages.value = true;
    errorMessages.value = [
      "An unexpected error occurred. Please try again later.",
    ];
  }
}

function clearFormData() {
  formData.value.title = "";
  formData.value.description = "";
  formData.value.poster = null;
}

onMounted(async () => {
  await getCsrfToken();
});

async function getCsrfToken() {
  try{
    const response = await fetch('/api/v1/csrf-token', {
    });
    const data = await response.json();
    csrfToken.value = data.csrf_token;
  } catch (error) {
    console.error("Error fetching CSRF token:", error);
  }
}
</script>

<style>
h1{
  margin-left:50px;
}
form{
    margin: 35px;
    margin-left: 50px;
}
label{
    display: block;
    font-size: 18px;
    font-weight: 500;
    margin-bottom: 10px;
}
input, textarea{
    max-width: 700px;
    width: 100%;
}
textarea{
  height:100px;
}

button{
  margin-top:12px;
}
</style>