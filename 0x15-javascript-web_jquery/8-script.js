$(function(){
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(res){
    for (let i = 0; i < res.results.length; i++){
      $('UL#list_movies').append(`<li>${res.results[i].title}</li>`)
    }
  })
})
