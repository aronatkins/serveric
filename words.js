function words() {
  var data = $("textarea").val().trim().split("\n");
  console.log("data",data);
  $.post( "/words", JSON.stringify(data), function( result ) {
    console.log("result",result);

    
    $("#words").html(result.words);
    $("#characters").html(result.characters);
    $("#vowels").html(result.vowels);
    $("#consonants").html(result.consonants);
    $("#results").toggle(true);
    
  }, "json");
}

$(function() {
  $("#results").toggle(false);

  $("form").submit(function(event) {
    words();
    event.preventDefault();
  });
});
