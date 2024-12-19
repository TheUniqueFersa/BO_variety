<?php
    //PETICIONES POSIBLES
    $climas = array(
        "frío" => "Bogotá",
        "calido" => "Montería",
        "templado" => "Medellín"
    );
    $paises_n = array("Guajira", "USA", "Canada", "Noruega", "Rusia");
    $paises_s = array("Leticia", "Arg", "Chile", "Madagascar", "Australia");
    $paises_e = array("Santander", "India", "China", "Japón", "Korea");
    $paises_o = array("Antioquia", "México", "Guatemala", "Brazil", "Venezuela");
    $ubi = array(
        "norte" => $paises_n,
        "sur" => $paises_s,
        "este" => $paises_e,
        "oeste" => $paises_o
    );
    $turismo = array(
        "mar" => "Santa Marta",
        "llano" => "Villavicencio",
        "desierto" => "Riohacha",
        "Valle" => "Quindío"
    );
    $tipo = "clima";
    $tipo = "ubicacion";
    $tipo = "turismo";
    $busqueda = "frío";
    $busqueda = "calido";
    $busqueda = "templado";
    // $busqueda = "norte";
    // $busqueda = "sur";
    // $busqueda = "este";
    // $busqueda = "oeste";
    // $busqueda = "mar";
    // $busqueda = "llano";
    $busqueda = "desierto";
    // $busqueda = "Valle";
    // -------------------------------------------
    
    if ($tipo == "clima") {
        $busq = $climas;
    } elseif ($tipo == "ubicacion") {
        $busq = $ubi;
    } else {
        $busq = $turismo;
    }
    // print_r($tipo == "clima");
    // print_r($busq);
    foreach ($busq as $key => $value) {
        if($tipo == "ubicacion" && $key == $busqueda){
            foreach ($value as $k => $val) {
                echo $val."<br>";
            }
        } else if($tipo != "ubicacion"){
            // print($key);
            // print($busqueda);
            if($key == $busqueda)
                echo $value;
        }
    }
    // -------------------------------------------
    // $busq = ($tipo == "clima")? $climas : ($tipo == "ubicacion")? $ubi : $turismo; -> POR ALGUN MOTIVO NO FUNCIONA ASÍ
    
?>