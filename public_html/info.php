<h1>Pierwsza storna w PHP</h1>
<?php // znacznik otweirający skrypt php
    //phpinfo();
    print_r($_POST);
 ?>
 <!-- znacznik zamykający skrypt  -->
<h2>Informacje nt. wersji PHP</h2>
<form name="formularz" id="formularz" method="POST">
  <table class="table">
      <tr>
        <td><label for="imie">Imię:</label></td>
        <td><input type="text" name="imie" value=""></td>
      </tr>
      <tr>
        <td><label for="nazwisko">Nazwisko:</label></td>
        <td><input type="text" name="nazwisko" value=""></td>
      </tr>
</table>

<fieldset>
  <legend>Wybierz płeć</legend>
  <input type="radio" name="gender" value="m"> Mężczyzna<br>
  <input type="radio" name="gender" value="k"> Kobieta<br>
  <input type="radio" name="gender" value="i" checked> Inny
</fieldset>
<fieldset>
  <legend>Wybierz pojazd</legend>
  <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
  <input type="checkbox" name="vehicle2" value="Car"> I have a car
</fieldset>
<select name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Cytryna</option>
  <option value="fiat">Fiat</option>
  <option value="audi" selected>Audi</option>
</select>
<select name="cars2" multiple>
  <option value="volvo">Volvo</option>
  <option value="saab">Cytryna</option>
  <option value="fiat">Fiat</option>
  <option value="audi" selected>Audi</option>
</select>
<br>
<textarea name="message" rows="10" cols="30">Iks kurde d</textarea>
<br>
<input type="submit" name="" value="Prześlij">
<input type="reset" name="" value="Resetuj">
</form>
