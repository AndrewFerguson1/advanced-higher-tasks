<?php
// Check if form values exist before using them
if (isset($_POST['name']) && isset($_POST['age']) && isset($_POST['favourite_game']) && isset($_POST['comments'])) {
    $name = $_POST['name'];
    $age = $_POST['age'];
    $favourite_game = $_POST['favourite_game'];
    $comments = $_POST['comments'];

    echo "<h1>Hello, $name!</h1>";
    echo "<p>You are $age years old.</p>";
    echo "<p>Your favourite game is: $favourite_game</p>";
    echo "<textarea>Your comments: $comments</textarea>";
} else {
    echo "No form data received.";
}
?>
