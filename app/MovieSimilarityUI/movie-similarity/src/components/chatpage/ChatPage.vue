<template>
    <spinner v-if="loading"/>
    <div v-if="data.results.length === 0" class="background-text">
        Search for a Movie Recommendantion
    </div>
    <div v-else class="results">
        <div v-for="result in data.results">
            <div class="description">{{result.description}}</div>
            <div class="result-movies">
                <div v-for="(movie, index) in result.movies" class="movie-wrapper">
                    <a :href="movie.imdb_url" target="_blank">
                        <img :src="movie.poster_url" width="45" height="67">
                    </a>
                    <div>
                        <span class="movie-title">
                            {{index+1}}. {{ movie.name }} 
                        </span>
                        <span class="date-published">
                            ({{movie.date_published}})
                        </span>
                        <span class="genre" v-for="genre in movie.genre">{{ genre }}</span>
                        <div>{{ movie.description }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="input-wrapper">
        <form  @submit.prevent="onSubmit">
        <input type="text" id="description" v-model="data.description" placeholder="Type a description for a Movie recomendation" >
        </form>
    </div>

  </template>

<script setup>
import { reactive, ref } from 'vue';
import axios from 'axios'
import Spinner from '../Spinner.vue'

const loading = ref(false);

const data = reactive({
  description: '',
  results:  []
})

async function onSubmit() {
    loading.value = true;
    axios.post(`http://localhost:5000/movies/top-five`, {
            description: data.description
        })
        .then(function(response) {
            if(response.data.movies){
                data.results.push({ description: data.description, movies: response.data.movies})
                data.description = ""
            }
            loading.value = false;
        })
        .catch(function(error) {
            console.log(error);
            loading.value = false;
        })
}

</script>


<style scoped>

.input-wrapper{
    margin: 30px 50px;
}

input {
    width: 100%;
    padding: 10px;
    border: #193f6e 1px solid;
    border-radius: 6px;
    box-shadow: 0 0 10px 5px #0076b620;
    outline: none;
}

.background-text{
    display: flex;
    flex-grow: 1;
    align-items: center;
    justify-content: center;
    text-shadow: 1px 1px 20px #193f6e;
}

.description {
    padding: 20px 50px;
}

.results {
    overflow-y: auto;
    overflow-x: hidden;
}

.result-movies{
    padding: 10px 50px;
    background-color: #e1ebec;
    border-top: #193f6e 1px solid;
    border-bottom: #193f6e 1px solid;
}

.movie-title{
    font-weight: bold;
}

.movie-wrapper{
    display: flex;
    gap: 10px;
}

.movie-wrapper:not(:last-child){
    margin-bottom: 10px;
    padding-bottom: 10px;
    border-bottom: white 3px solid;
}

.date-published{
    margin-right: 20px;
}

.genre {
    font-weight: 600;
    border: #193f6e 1px solid;
    padding-left: 5px;
    padding-right: 5px;
    border-radius: 10px;
    margin-right: 10px;
}
</style>