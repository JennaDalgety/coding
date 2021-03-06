$(".loc").hover(
    function() {
        $(this).html("<strong>Location:</strong> Your house?!");
    },
    function() {
        $(this).html("<strong>Location:</strong> Treehouse Adoption Center");
});


//Adds a pet to the page with user input
$("#add-pet").on("click", function() {
    //Grab info from the form
    let $name = $("#pet-name");
    let $species = $("#pet-species");
    let $notes = $("#pet-notes");

    //Assemble the HTML of our new element with the above variables
    let $newPet = $(
        '<section class="six columns"><div class="card"><p><strong>Name:</strong> ' + $name.val() +
        '</p><p><strong>Species:</strong> ' + $species.val() +
        '</p><p><strong>Notes:</strong> ' + $notes.val() +
        '</p><span class="close">&times;</span></div></section>'
    );

    //Attach the new element to the page
    $("#posted-pets").append($newPet);

});

//Puppy images fade in
$("img").css("display", "none").fadeIn(1600);

$(".card").on("click", function() {
    $(this).toggleClass("selected");
});