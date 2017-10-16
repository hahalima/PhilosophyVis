var wikiParser = require('wiki-infobox-parser');
var fs = require('fs');

var philosophers = ["Thales of Miletus","Pherecydes of Syros","Anaximander","Anaximenes of Miletus","Pythagoras","Xenophanes","Epicharmus of Kos","Heraclitus","Parmenides","Anaxagoras","Empedocles","Zeno of Elea","Protagoras","Sophistic works of Antiphon","Hippias","Gorgias","Socrates","Critias","Prodicus","Leucippus","Thrasymachus","Democritus","Diagoras of Melos","Antisthenes","Aristippus","Alcidamas","Lycophron (sophist)","Diogenes of Apollonia","Hippo (philosopher)","Xenophon","Plato","Speusippus","Eudoxus of Cnidus","Diogenes","Xenocrates","Aristotle","Archelaus (philosopher)","Melissus of Samos","Cratylus","Ion of Chios","Echecrates","Timaeus of Locri","Theophrastus","Pyrrho","Strato of Lampsacus","Epicurus","Zeno of Citium","Timon of Phlius","Chrysippus","Carneades","Lucretius","Cicero","Philo","Seneca the Younger","Epictetus","Marcus Aurelius","Sextus Empiricus","Plotinus","Porphyry (philosopher)","Iamblichus","Augustine of Hippo","Proclus","Boethius","John Philoponus","Al-Kindi","John Scotus Eriugena","Al-Faràbi","Saadia Gaon","Al-Razi","Avicenna","Solomon ibn Gabirol","Anselm of Canterbury","Al-Ghazali","Peter Abelard","Abraham ibn Daud","Peter Lombard","Averroes","Maimonides","Francis of Assisi","Robert Grosseteste","Albertus Magnus","Roger Bacon","Thomas Aquinas","Bonaventure","Siger of Brabant","Ramon Llull","Meister Eckhart","Duns Scotus","Marsilius of Padua","William of Ockham","Gersonides","Jean Buridan","John Wycliffe","Nicole Oresme","Hasdai Crescas","Gemistus Pletho","Nicholas of Cusa","Lorenzo Valla","Marsilio Ficino","Giovanni Pico della Mirandola","Boetius of Dacia","Erasmus","Niccolò Machiavelli","Thomas More","Martin Luther","Petrus Ramus","John Calvin","Michel de Montaigne","Pierre Charron","Giordano Bruno","Francisco Suarez","Francis Bacon","Galileo Galilei","Hugo Grotius","François de La Mothe Le Vayer","Marin Mersenne","Robert Filmer","Pierre Gassendi","René Descartes","Baltasar Gracián","Thomas Hobbes","Antoine Arnauld","Henry More","Jacques Rohault","Ralph Cudworth","Blaise Pascal","Margaret Cavendish, Duchess of Newcastle-upon-Tyne","Arnold Geulincx","Pierre Nicole","Géraud de Cordemoy","Robert Boyle","Anne Conway (philosopher)","Richard Cumberland (philosopher)","Baruch Spinoza","Samuel von Pufendorf","John Locke","Joseph Glanvill","Nicolas Malebranche","Isaac Newton","Simon Foucher","Pierre Bayle","Damaris Cudworth Masham","John Toland","Gottfried Wilhelm Leibniz","John Norris (philosopher)","Jean Meslier","Giambattista Vico","Bernard Mandeville","Anthony Ashley-Cooper, 3rd Earl of Shaftesbury","Samuel Clarke","Catherine Trotter Cockburn","Christian Wolff (philosopher)","George Berkeley","Montesquieu","Joseph Butler","Francis Hutcheson (philosopher)","John Gay (philosopher)","David Hartley (philosopher)","Julien Offray de La Mettrie","Voltaire","Thomas Reid","David Hume","Jean-Jacques Rousseau","Denis Diderot","Alexander Gottlieb Baumgarten","Claude Adrien Helvétius","Étienne Bonnot de Condillac","Jean le Rond d'Alembert","Baron d'Holbach","Adam Smith","Richard Price","Immanuel Kant","Moses Mendelssohn","Gotthold Ephraim Lessing","Edmund Burke","William Paley","Thomas Jefferson","Jeremy Bentham","Sylvain Maréchal","Dugald Stewart","William Godwin","Mary Wollstonecraft","Friedrich Schiller","Johann Gottlieb Fichte","Edward Herbert, 1st Baron Herbert of Cherbury","Jean-Baptiste Lamarck","Pierre-Simon Laplace","Joseph de Maistre","Claude Henri de Rouvroy, comte de Saint-Simon","Germaine de Staël","Friedrich Schleiermacher","Georg Wilhelm Friedrich Hegel","James Mill","Friedrich Wilhelm Joseph Schelling","Bernard Bolzano","Richard Whately","Arthur Schopenhauer","John Austin (legal philosopher)","William Whewell","Auguste Comte","Ralph Waldo Emerson","Ludwig Feuerbach","Alexis de Tocqueville","Max Stirner","Augustus De Morgan","John Stuart Mill","Pierre-Joseph Proudhon","Charles Darwin","Margaret Fuller","Søren Kierkegaard","Henry David Thoreau","Sir William Hamilton, 9th Baronet","Sojourner Truth","Harriet Taylor Mill","Mikhail Bakunin","Elizabeth Cady Stanton","Hermann Lotze","Karl Marx","Friedrich Engels","Herbert Spencer","Susan B. Anthony","Wilhelm Dilthey","Edward Caird","Thomas Hill Green","Henry Sidgwick","Ernst Mach","Franz Brentano","Charles Sanders Peirce","William James","Peter Kropotkin","Friedrich Nietzsche","William Kingdon Clifford","F.H. Bradley","Vilfredo Pareto","Bernard Bosanquet (philosopher)","Gottlob Frege","John Cook Wilson","Hans Vaihinger","David George Ritchie","Alexius Meinong","Henri Poincaré","Josiah Royce","Andrew Seth Pringle-Pattison","Ferdinand de Saussure","Émile Durkheim","Giuseppe Peano","Edmund Husserl","Samuel Alexander","Henri Bergson","John Dewey","Jane Addams","Pierre Duhem","Karl Groos","Alfred North Whitehead","George Herbert Mead","Max Weber","Miguel de Unamuno","J. M. E. McTaggart","Benedetto Croce","Emma Goldman","Rosa Luxemburg","G.E. Moore","Martin Buber","George Santayana","Harold Arthur Prichard","Bertrand Russell","Arthur Oncken Lovejoy","Nikolai Berdyaev","Ernst Cassirer","Max Scheler","Giovanni Gentile","Ralph Barton Perry","W.D. Ross","Pierre Teilhard de Chardin","Hans Kelsen","Moritz Schlick","Otto Neurath","Nicolai Hartmann","Jacques Maritain","José Ortega y Gasset","Clarence Irving Lewis","Gaston Bachelard","Georg Lukács","Walter Terence Stace","Karl Barth","C. D. Broad","Ludwig Wittgenstein","Gabriel Marcel","Martin Heidegger","Antonio Gramsci","Rudolf Carnap","Walter Benjamin","Brand Blanshard","F. S. C. Northrop","Roman Ingarden","Susanne Langer","Friedrich Waismann","Georges Bataille","Herbert Marcuse","Xavier Zubiri","Leo Strauss","H.H. Price","Gilbert Ryle","Hans-Georg Gadamer","Jacques Lacan","Alfred Tarski","Ernest Nagel","Karl Popper","Mortimer J. Adler","Frank P. Ramsey","Theodor W. Adorno","Ernest Addison Moody","Jean-Paul Sartre","Karl Jaspers","Eugen Fink","Ayn Rand","Kurt Gödel","Emmanuel Levinas","Hannah Arendt","H.L.A. Hart","Charles Stevenson","Maurice Merleau-Ponty","Simone de Beauvoir","Willard van Orman Quine","Simone Weil","A.J. Ayer","J.L. Austin","Marshall McLuhan","Alan Turing","Wilfrid Sellars","Albert Camus","Paul Ricœur","Roland Barthes","J. L. Mackie","Donald Davidson (philosopher)","Louis Althusser","R. M. Hare","P. F. Strawson","John Rawls","Zygmunt Bauman","Frantz Fanon","Gilles Deleuze","Michel Foucault","Hilary Putnam","David Malet Armstrong","John Howard Yoder","Noam Chomsky","Bernard Williams","Jean Baudrillard","Jürgen Habermas","Jaakko Hintikka","Alasdair MacIntyre","Allan Bloom","Pierre Bourdieu","Jacques Derrida","Guy Debord","Richard Rorty","Charles Taylor (philosopher)","John Searle","Alvin Plantinga","Jerry Fodor","Robert M. Pirsig","Thomas Nagel","Alain Badiou","Robert Nozick","Tom Regan","Saul Kripke","Jean-Luc Nancy","David Lewis (philosopher)","Joxe Azurmendi","Derek Parfit","Giorgio Agamben","Gayatri Chakravorty Spivak","Peter Singer","John Ralston Saul","Slavoj Žižek","Ken Wilber","Cornel West","Judith Butler","Alexander Wendt"];

var test = [];

//writes all the json objects containing philosopher data to unsortedinfoboxdata.txt
var writeStream = fs.createWriteStream('unsortedInfoboxData.txt');
for (var i = 0; i < philosophers.length; i++) {
  getInfoboxData(i, philosophers[i]);
}

function getInfoboxData(phil_id, philosopher_name) {
  wikiParser(philosopher_name, function(err, result) {
    if (err) {
      var myObj = {};
          if (err.message == "Infobox Not Found") {
            test.push("res");
            myObj.name = philosopher_name;
            myObj.influences = null;
            myObj.influenced = null;
            myObj.wikiErrorMessage = "Infobox Not Found";
            myObj.id = phil_id;
          }
          if (err.message == "Page Index Not Found") {
            test.push("res");
            myObj.name = philosopher_name;
            myObj.influences = null;
            myObj.influenced = null;
            myObj.wikiErrorMessage = "Page Index Not Found";
            myObj.id = phil_id;
          }
        // console.log(JSON.stringify(myObj) + ",");
        var result = (JSON.stringify(myObj) + ",");
        writeStream.write(result, 'utf-8');
    } else {
          res = JSON.parse(result);
          if (res.name == undefined) {
            res["name"] = philosopher_name;
          }
          if (res.influences == undefined) {
            res["influences"] = null;
          }
          if (res.influenced == undefined) {
            res["influenced"] = null;
          }
          test.push("res");
          res.id = phil_id;
          // console.log(philosopher_name);
          // console.log(JSON.stringify(res) + ",");
          var result = (JSON.stringify(res) + ",");
          writeStream.write(result, 'utf-8');
      }
  });
}

//to check if all 380 philosophers are accessed
var delayMillis = 5000; //5 second
setTimeout(function() {
  console.log(philosophers.length);
  console.log(test.length);
  writeStream.end('end');

}, delayMillis);

//After turning the unsortedInfoboxData.txt from earlier into a json file,
//below sorted the data by id and stores it in sortedInfoboxData.txt and will convert it to json file
// console.log("\n *STARTING* \n");
// // Get content from file
// var contents = fs.readFileSync("unsortedInfoboxData.json");
// // Define to JSON type
// var jsonContent = JSON.parse(contents);
//
// var sorted = jsonContent.philosophers.sort(function (a, b) {
//   return a.id - b.id;
// });
//
// var result = ""
// for (i = 0; i < sorted.length; i++) {
//   var result = result + (JSON.stringify(sorted[i]) + ",");
// }
//
// //write to file
// var stream = fs.createWriteStream("sortedInfoboxData.txt");
// stream.once('open', function(fd) {
//   stream.write(result);
//   stream.end();
// });
// console.log("\n *ENDING* \n");
