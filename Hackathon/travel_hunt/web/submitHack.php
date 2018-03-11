<?php
    //checking if data has been entered
    if( isset( $_POST['content'] ) && !empty( $_POST['content'] ) )
    {
        $data = $_POST['content'];
    } else {
        header( 'location: form.html' );
        exit();
    }

    //setting up mysql details
    $sql_server = 'iradinsky@ada.sterncs.net';
    $sql_user = 'uiradinsk';
    $sql_pwd = 'p2253';
    $sql_db = 'diradinsk';

    //connecting to sql database
    $myslqi = new mysqli( $sql_server, $sql_user, $sql_pwd, $sql_db ) or die( $mysqli->error );

    //inserting details into table
    $insert = $mysqli->query( "INSERT INTO table ( `Hacks` ) VALUE ( '$content' )" );

    //closing mysqli connection
    $mysqli->close;
?>