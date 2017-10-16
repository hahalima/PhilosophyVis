# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import wikipedia
import wptools
import csv
import re

greeksWithDates = """Thales of Miletus (c. 624 546 BC). Of the Milesian school. Believed that all was made of water.
Pherecydes of Syros (c. 620 - c. 550 BC). Cosmologist.
Anaximander (c. 610 – 546 BC). Of the Milesian school. Famous for the concept of Apeiron, or "the boundless".
Anaximenes of Miletus (c. 585 – 525 BC). Of the Milesian school. Believed that all was made of air.
Pythagoras (c. 580 – c. 500 BC). Of the Ionian School. Believed the deepest reality to be composed of numbers, and that souls are immortal.
Xenophanes (c. 570 – 480 BC). Sometimes associated with the Eleatic school.
Epicharmus of Kos (c. 530 – 450 BC). Comic playwright and moralist.
Heraclitus (c. 535 – c. 475 BC). Of the Ionians. Emphasized the order and mutability of the universe.
Parmenides (c. 515 – 450 BC). Of the Eleatics. Reflected on the concept of Being.
Anaxagoras (c. 500 – 428 BC). Of the Ionians. Pluralist.
Empedocles (492 - 432 BC). Eclectic cosmogonist. Pluralist.
Zeno of Elea (c. 490 – 430 BC). Of the Eleatics. Known for his paradoxes.
Protagoras (c. 481 – 420 BC). Sophist. Early advocate of relativism.
Sophistic works of Antiphon (480 - 411 BC). Sophist.
Hippias (Middle of the 5th century BC). Sophist.
Gorgias (c. 483 – 375 BC). Sophist. Early advocate of solipsism.
Socrates (c. 470 – 399 BC). Emphasized virtue ethics. In epistemology, understood dialectic to be central to the pursuit of truth.
Critias (c. 460 - 413 BC). Atheist writer and politician.
Prodicus (c. 465 – c. 395 BC). Sophist.
Leucippus (First half of the 5th century BC). Founding Atomist, Determinist.
Thrasymachus (c. 459 - c. 400 BC). Sophist.
Democritus (c. 450 – 370 BC). Founding Atomist.
Diagoras of Melos (c. 450 – 415 BC). Atheist.
Antisthenes (c. 444 – 365 BC). Founder of Cynicism. Pupil of Socrates.
Aristippus (c. 440 – 366 BC). A Cyrenaic. Advocate of ethical hedonism.
Alcidamas (c. 435 – c. 350 BC). Sophist.
Lycophron (Sophist) c. 430 – c. 350 BC). Sophist.
Diogenes of Apollonia (c. 425 BC – c 350 BC). Cosmologist.
Hippo (c. 425 – c 350 BC). Atheist cosmologist.
Xenophon (c. 427 – 355 BC). Historian.
Plato (c. 427 – 347 BC). Famed for view of the transcendental forms. Advocated polity governed by philosophers.
Speusippus (c. 408 – 339 BC). Nephew of Plato.
Eudoxus of Cnidus (c. 408 – 355 BC). Pupil of Plato.
Diogenes (c. 399 – 323 BC). Cynic.
Xenocrates (c. 396 – 314 BC). Disciple of Plato.
Aristotle (c. 384 – 322 BC). A polymath whose works ranged across all philosophical fields.
"""

greeksWithPeriods = """Archelaus. A pupil of Anaxagoras.
Melissus of Samos. Eleatic.
Cratylus. Follower of Heraclitus.
Ion of Chios. Pythagorean cosmologist.
Echecrates. Pythagorean.
Timaeus of Locri. Pythagorean.
"""

hellenisticEra = """Theophrastus (c. 371 BC–c. 287 BC). Peripatetic.
Pyrrho (c. 360 – 270 BC). Skeptic.
Strato of Lampsacus (c. 340 BC–c. 268 BC). Atheist, Materialist.
Epicurus (c. 341 – 270 BC). Materialist Atomist, hedonist. Founder of Epicureanism
Zeno of Citium (c. 333 – 264 BC). Founder of Stoicism.
Timon of Phlius (c. 320 – 230 BC). Pyrrhonist, skeptic.
Chrysippus (c. 280 – 207 BC). Major figure in Stoicism.
Carneades (c. 214 – 129 BC). Academic skeptic. Understood probability as the purveyor of truth.
"""

romanEra = """Lucretius (c. 99 – 55 BC). Epicurean.
Cicero (c. 106 BC – 43 BC) Political theorist.
Philo (c. 20 BC – 40 AD). Believed in the allegorical method of reading texts.
Seneca the Younger (c. 4 BC – 65 AD). Stoic.
Epictetus (c. 55 – 135). Stoic. Emphasized ethics of self-determination.
Marcus Aurelius (121–180). Stoic.
Sextus Empiricus (fl. during the 2nd and possibly the 3rd centuries AD). Skeptic, Pyrrhonist.
Plotinus (c. 205 – 270). Neoplatonist. Had a holistic metaphysics.
Porphyry (c. 232 – 304). Student of Plotinus.
Iamblichus (c. 245 – 325). Late neoplatonist. Espoused theurgy.
Augustine of Hippo (c. 354 – 430). Original Sin. Church father.
Proclus (c. 412 – 485). Neoplatonist.
"""

medievalWithDates = """Boethius (c. 480–524).
John Philoponus (c. 490–570).
Al-Kindi (c. 801 – 873). Major figure at Islamic philosophy. Influenced by Neoplatonism.
John Scotus Eriugena (c. 815 – 877). neoplatonist, pantheist.
Al-Faràbi (c. 870 – 950). Major Islamic philosopher. Neoplatonist.
Saadia Gaon (c. 882 – 942).
Al-Razi (c. 865 – 925). Rationalist. Major Islamic philosopher. Held that God creates universe by rearranging pre-existing laws.
Avicenna (c. 980 – 1037). Major Islamic philosopher.
Solomon ibn Gabirol (Avicebron) (c. 1021–1058). Jewish philosopher.
Anselm of Canterbury (c. 1034–1109). Christian philosopher. Produced ontological argument for the existence of God.
Al-Ghazali (c. 1058–1111). Islamic philosopher. Mystic.
Peter Abelard (c. 1079–1142). Scholastic philosopher. Dealt with problem of universals.
Abraham ibn Daud (c. 1110–1180). Jewish philosophy.
Peter Lombard (c. 1100–1160). Scholastic.
Averroes (Ibn Rushd, "The Commentator") (c. 1126-December 10, 1198). Islamic philosopher.
Maimonides (c. 1135–1204). Jewish philosophy.
Francis of Assisi (c. 1182–1226). Ascetic.
Robert Grosseteste (c. 1175–1253).
Albertus Magnus (c. 1193–1280). Early Empiricist.
Roger Bacon (c. 1214–1294). Empiricist, mathematician.
Thomas Aquinas (c. 1221–1274). Christian philosopher.
Bonaventure (c. 1225–1274). Franciscan.
Siger of Brabant (c. 1240 – c. 1280). Averroist.
Ramon Llull (c. 1232–1315) Catalan philosopher
Meister Eckhart (c. 1260–1328). mystic.
Duns Scotus (c. 1266–1308). Franciscan, Scholastic, Original Sin.
Marsilius of Padua (c. 1270–1342). Understood chief function of state as mediator.
William of Ockham (c. 1288–1348). Franciscan. Scholastic. Nominalist, creator of Ockham's razor.
Gersonides (c. 1288–1344). Jewish philosopher.
Jean Buridan (c. 1300–1358). Nominalist.
John Wycliffe (c. 1320–1384).
Nicole Oresme (c. 1320-5 – 1382). Made contributions to economics, science, mathematics, theology and philosophy.
Hasdai Crescas (c. 1340 – c. 1411). Jewish philosopher.
Gemistus Pletho (c. 1355 – 1452/1454). Late Byzantine scholar of neoplatonic philosophy.
Nicholas of Cusa (1401–1464). Christian philosopher.
Lorenzo Valla (1407–1457). Humanist, critic of scholastic logic.
Marsilio Ficino (1433-1499). Christian Neoplatonist, head of Florentine Academy and major Renaissance Humanist figure. First translator of Plato's complete extant works into Latin.
Giovanni Pico della Mirandola (1463–1494). Renaissance humanist.
"""

medievalWithPeriods = """Boetius of Dacia. Averroist, Aristotelian.
"""

earlyModernWithDates = """Erasmus (1466–1536). Humanist, advocate of free will.
Niccolò Machiavelli (1469–1527). Political realism.
Thomas More (1478–1535). Humanist, created term "utopia".
Martin Luther (1483–1546). Major Western Christian theologian.
Petrus Ramus (1515–1572).
John Calvin (1509–1564). Major Western Christian theologian.
Michel de Montaigne (1533–1592). Humanist, skeptic.
Pierre Charron (1541–1603).
Giordano Bruno (1548–1600). Advocate of heliocentrism.
Francisco Suarez (1548–1617). Politically proto-liberal.
Francis Bacon (1561–1626). Empiricist.
Galileo Galilei (1564–1642). Heliocentrist.
Hugo Grotius (1583–1645). Natural law theorist.
François de La Mothe Le Vayer (1588-1672)
Marin Mersenne (1588–1648). Cartesian.
Robert Filmer (1588–1653).
Pierre Gassendi (1592–1655). Mechanicism. Empiricist.
René Descartes (1596–1650). Heliocentrism, dualism, rationalism.
Baltasar Gracián (1601–1658). Spanish catholic philosopher
Thomas Hobbes (1588–1679). Political realist.
Antoine Arnauld (1612–1694).
Henry More (1614–1687).
Jacques Rohault (1617–1672) Cartesian.
Ralph Cudworth (1617–1688). Cambridge Platonist.
Blaise Pascal (1623–1662). Physicist, scientist. Noted for Pascal's wager.
Margaret Cavendish, Duchess of Newcastle-upon-Tyne (1623–1673). Materialist, feminist.
Arnold Geulincx (1624–1669). Important occasionalist theorist.
Pierre Nicole (1625–1695).
Géraud de Cordemoy (1626-1684). Dualist.
Robert Boyle (1627–1691).
Anne Conway (1631–1679).
Richard Cumberland (1631–1718). Early proponent of utilitarianism.
Baruch Spinoza (1632–1677).
Samuel von Pufendorf (1632–1694). Social contract theorist.
John Locke (1632–1704). Major Empiricist. Political philosopher.
Joseph Glanvill (1636–1680).
Nicolas Malebranche (1638–1715). Cartesian.
Isaac Newton (1643–1727).
Simon Foucher (1644–1696). Skeptic.
Pierre Bayle (1647–1706). Pyrrhonist.
Damaris Cudworth Masham (1659–1708).
John Toland (1670–1722).
Gottfried Wilhelm Leibniz (1646–1716). Co-inventor of calculus.
John Norris (1657–1711). Malebranchian.
Jean Meslier (1664-1729)
Giambattista Vico (1668–1744).
Bernard Mandeville (1670–1733).
Anthony Ashley-Cooper, 3rd Earl of Shaftesbury (1671–1713).
Samuel Clarke (1675–1729).
Catherine Trotter Cockburn (1679–1749).
Christian Wolff (1679–1754). Determinist, rationalist.
George Berkeley (1685–1753). Idealist, empiricist.
Montesquieu (1689–1755). Skeptic, humanist.
Joseph Butler (1692–1752).
Francis Hutcheson (1694–1746). Proto-utilitarian.
John Gay (1699–1745).
David Hartley (1705–1757).
Julien Offray de La Mettrie (1709–1751). Materialist, genetic determinist.
Voltaire (1694–1778). Advocate for freedoms of religion and expression.
Thomas Reid (1710–1796). Member of Scottish Enlightenment, founder of Scottish Common Sense philosophy.
David Hume (1711–1776). Empiricist, skeptic.
Jean-Jacques Rousseau (1712–1778). Social contract political philosopher.
Denis Diderot (1713–1784).
Alexander Gottlieb Baumgarten (1714-1762).
Claude Adrien Helvétius (1715–1771). Utilitarian.
Étienne Bonnot de Condillac (1715-1780).
Jean le Rond d'Alembert (1717–1783).
Baron d'Holbach (1723–1789). Materialist, atheist.
Adam Smith (1723–1790). Economic theorist, member of Scottish Enlightenment.
Richard Price (1723–1791). Political liberal.
Immanuel Kant (1724–1804). Deontologist, proponent of synthetic a priori truths.
Moses Mendelssohn (1729–1786). Member of the Jewish Enlightenment.
Gotthold Ephraim Lessing (1729–1781).
Edmund Burke (1729–1797). Conservative political philosopher.
William Paley (1743–1805).
Thomas Jefferson (1743–1826). Liberal political philosopher.
Jeremy Bentham (1748–1832). Utilitarian, hedonist.
Sylvain Maréchal (1750–1803) Anarcho-communist, Deist
Dugald Stewart (1753–1828).
William Godwin (1756–1836). Anarchist, utilitarian.
Mary Wollstonecraft (1759–1797). Feminist.
Friedrich Schiller (1759–1805).
Johann Gottlieb Fichte (1762–1814).
"""

earlyModernWithPeriods = """Edward Herbert, 1st Baron Herbert of Cherbury. Nativist.
"""

modernEra = """Jean-Baptiste Lamarck (1744–1829). Early evolutionary theorist.
Pierre-Simon Laplace (1749–1827). Determinist.
Joseph de Maistre (1753–1821) Conservative
Claude Henri de Rouvroy, comte de Saint-Simon (1760–1825). Socialist.
Germaine de Staël (1766–1817).
Friedrich Schleiermacher (1768–1834). Hermeneutician.
Georg Wilhelm Friedrich Hegel (1770–1831). German idealist.
James Mill (1773–1836). Utilitarian.
Friedrich Wilhelm Joseph Schelling (1775–1854). German idealist.
Bernard Bolzano (1781–1848).
Richard Whately (1787–1863).
Arthur Schopenhauer (1788–1860). Pessimist.
John Austin (1790–1859). Legal positivist, utilitarian.
William Whewell (1794–1866).
Auguste Comte (1798–1857). Social philosopher, positivist.
Ralph Waldo Emerson (1803–1882). Transcendentalist, abolitionist, egalitarian, humanist.
Ludwig Feuerbach (1804–1872).
Alexis de Tocqueville (1805-1859).
Max Stirner (1806-1856). Anarchist.
Augustus De Morgan (1806–1871). Logician.
John Stuart Mill (1806–1873). Utilitarian.
Pierre-Joseph Proudhon (1809–1865). Anarchist.
Charles Darwin (1809–1882).
Margaret Fuller (1810–1850). Egalitarian.
Søren Kierkegaard (1813–1855). Existentialist.
Henry David Thoreau (1817–1862). Transcendentalist, pacifist, abolitionist.
Sir William Hamilton, 9th Baronet (1788–1856).
Sojourner Truth (c. 1797–1883). Egalitarian, abolitionist.
Harriet Taylor Mill (1807–1858). Egalitarian, utilitarian.
Mikhail Bakunin (1814–1876). Revolutionary anarchist.
Elizabeth Cady Stanton (1815–1902). Egalitarian.
Hermann Lotze (1817–1881).
Karl Marx (1818–1883). Socialist, formulated historical materialism.
Friedrich Engels (1820–1895). Egalitarian, dialectical materialist.
Herbert Spencer (1820–1903). Nativism, libertarianism, social Darwinism.
Susan B. Anthony (1820–1906). Feminist.
Wilhelm Dilthey (1833–1911).
Edward Caird (1835–1908). Idealist.
Thomas Hill Green (1836–1882). British idealist.
Henry Sidgwick (1838–1900). Rationalism, utilitarianism.
Ernst Mach (1838–1916). Philosopher of science, influence on logical positivism.
Franz Brentano (1838–1917). Phenomenologist.
Charles Sanders Peirce (1839–1914). Pragmatist.
William James (1842–1910). Pragmatism, Radical empiricism.
Peter Kropotkin (1942-1921). Anarchist communism.
Friedrich Nietzsche (1844–1900). Naturalistic philosopher, influence on Existentialism.
William Kingdon Clifford (1845–1879). Evidentialist.
F.H. Bradley (1846–1924). Idealist.
Vilfredo Pareto (1848–1923). Social philosopher.
Bernard Bosanquet (1848–1923). Idealist.
Gottlob Frege (1848–1925). Influential analytic philosopher.
John Cook Wilson (1849–1915).
Hans Vaihinger (1852–1933). Specialist in counterfactuals.
David George Ritchie (1853–1903). Idealist.
Alexius Meinong (1853–1920). Logical realist.
Henri Poincaré (1854–1912).
Josiah Royce (1855–1916). Idealist.
Andrew Seth Pringle-Pattison (1856–1931).
Ferdinand de Saussure (1857–1913). Linguist, Semiotics, Structuralism.
Émile Durkheim (1858–1917). Social philosopher.
Giuseppe Peano (1858–1932).
Edmund Husserl (1859–1938). Founder of phenomenology.
Samuel Alexander (1859–1938). Perceptual realist.
Henri Bergson (1859–1941).
John Dewey (1859–1952). Pragmatism.
Jane Addams (1860–1935). Pragmatist.
Pierre Duhem (1861–1916).
Karl Groos (1861-1946). Evolutionary instrumentalist theory of play.
Alfred North Whitehead (1861–1947). Process Philosophy, Mathematician, Logician, Philosophy of Physics, Panpsychism.
George Herbert Mead (1863–1931). Pragmatism, symbolic interactionist.
Max Weber (1864–1920). Social philosopher.
Miguel de Unamuno (1864–1936).
J. M. E. McTaggart (1866–1925). Idealist.
Benedetto Croce (1866–1952).
Emma Goldman (1869–1940). Anarchist.
Rosa Luxemburg (1870–1919). Marxist political philosopher.
G.E. Moore (1873–1958). Common sense theorist, ethical non-naturalist.
Martin Buber (1878–1965). Jewish philosopher, existentialist.
George Santayana (1863–1952). Pragmatism, naturalism; known for many aphorisms.
Harold Arthur Prichard (1871–1947). Moral intuitionist.
Bertrand Russell (1872–1970). Analytic philosopher, atheist, influential.
Arthur Oncken Lovejoy (1873–1962).
Nikolai Berdyaev (1874–1948). Existentialist.
Ernst Cassirer (1874–1945).
Max Scheler (1874-1928). German phenomenologist.
Giovanni Gentile (1875–1944). Idealist and fascist philosopher.
Ralph Barton Perry (1876–1957).
W.D. Ross (1877–1971). Deontologist.
Pierre Teilhard de Chardin (1881–1955). Christian evolutionist.
Hans Kelsen (1881–1973). Legal positivist.
Moritz Schlick (1882–1936). Founder of Vienna Circle, logical positivism.
Otto Neurath (1882–1945). Member of Vienna Circle.
Nicolai Hartmann (1882–1950).
Jacques Maritain (1882–1973). Human rights theorist.
José Ortega y Gasset (1883–1955). Philosopher of History.
Clarence Irving Lewis (1883–1964). Conceptual pragmatist.
Gaston Bachelard (1884–1962).
Georg Lukács (1885–1971). Marxist philosopher.
Walter Terence Stace (1886–1967)
Karl Barth (1886–1968).
C. D. Broad (1887–1971).
Ludwig Wittgenstein (1889–1951). Analytic philosopher, philosophy of language, philosophy of mind, influential.
Gabriel Marcel (1889–1973). Christian existentialist.
Martin Heidegger (1889–1976). Phenomenologist.
Antonio Gramsci (1891–1937). Marxist philosopher.
Rudolf Carnap (1891–1970). Vienna Circle. Logical positivist.
Walter Benjamin (1892-1940). Marxist. Philosophy of language.
Brand Blanshard (1892–1987).
F. S. C. Northrop (1893–1992). Epistemolog.
Roman Ingarden (1893–1970). Perceptual realist, phenomenalist.
Susanne Langer (1895–1985).
Friedrich Waismann (1896–1959). Vienna Circle. Logical positivist.
Georges Bataille (1897-1962).
Herbert Marcuse (1898–1979). Frankfurt School.
Xavier Zubiri (1898-1983). Materialist open realism.
Leo Strauss (1899–1973). Political Philosopher.
H.H. Price (1899–1984).
Gilbert Ryle (1900–1976).
Hans-Georg Gadamer (1900–2002). Hermeneutics.
Jacques Lacan (1901–1981). Structuralism.
Alfred Tarski (1901–1983). Created T-Convention in semantics.
Ernest Nagel (1901–1985). Logical positivist.
Karl Popper (1902–1994). Falsificationist.
Mortimer J. Adler (1902–2001).
Frank P. Ramsey (1903–1930). Proposed redundancy theory of truth.
Theodor W. Adorno (1903–1969). Frankfurt School.
Ernest Addison Moody (1903–1975).
Jean-Paul Sartre (1905–1980). Humanism, existentialism.
Karl Jaspers (1905–1982). Existentialist.
Eugen Fink (1905–1975). Phenomenologist.
Ayn Rand (1905–1982). Objectivist, Individualist.
Kurt Gödel (1906–1978). Vienna Circle.
Emmanuel Levinas (1906-1995).
Hannah Arendt (1906–1975). Political Philosophy.
H.L.A. Hart (1907–1992). Legal positivism.
Charles Stevenson (1908–1979).
Maurice Merleau-Ponty (1908-1961). Influential French phenomenologist.
Simone de Beauvoir (1908–1986). Existentialist, feminist.
Willard van Orman Quine (1908–2000).
Simone Weil (1909–1943).
A.J. Ayer (1910–1989). Logical positivist, emotivist.
J.L. Austin (1911–1960).
Marshall McLuhan (1911–1980). Media theory.
Alan Turing (1912–1954). Functionalist in philosophy of mind.
Wilfrid Sellars (1912-1989). Influential American philosopher
Albert Camus (1913–1960). Absurdist.
Paul Ricœur (1913-2005). French philosopher and theologian.
Roland Barthes (1915-1980). French semiotician and literary theorist.
J. L. Mackie (1917–1981). Moral skeptic.
Donald Davidson (1917–2003).
Louis Althusser (1918-1990).
R. M. Hare (1919–2002).
P. F. Strawson (1919–2006).
John Rawls (1921–2002). Liberal.
Zygmunt Bauman (1925-2017). Polish sociologist and philosopher, who introduced the idea of liquid modernity.
Frantz Fanon (1925–1961). Post-colonialism
Gilles Deleuze (1925-1995). Post-structuralism
Michel Foucault (1926–1984). Structuralism, Post-structuralism, Postmodernism, Queer theory.
Hilary Putnam (1926-2016).
David Malet Armstrong (born 1926).
John Howard Yoder (1927–1997). Pacifist.
Noam Chomsky (born 1928).
Bernard Williams (1929-2003). Moral philosopher.
Jean Baudrillard (1929–2007). Postmodernism, Post-structuralism.
Jürgen Habermas (born 1929).
Jaakko Hintikka (born 1929).
Alasdair MacIntyre (born 1929). Aristotelian.
Allan Bloom (1930–1992). Political Philosopher.
Pierre Bourdieu (1930-2002). French psychoanalytic sociologist and philosopher.
Jacques Derrida (1930–2004). Deconstruction.
Guy Debord (1931-1994). French Marxist philosopher.
Richard Rorty (1931–2007). Pragmatism, Postanalytic philosophy.
Charles Taylor (born 1931). Political philosophy, Philosophy of Social Science, and Intellectual History
John Searle (born 1932).
Alvin Plantinga (born 1932). Reformed epistemology, Philosophy of Religion.
Jerry Fodor (born 1935).
Robert M. Pirsig (born 1935). Introduced the Methaphysics of Quality. MOQ incorporates facets of East Asian philosophy, pragmatism and the work of F. S. C. Northrop.
Thomas Nagel (born 1937).
Alain Badiou (born 1937).
Robert Nozick (1938–2002). Libertarian.
Tom Regan (born 1938) animal rights philosopher
Saul Kripke (born 1940).
Jean-Luc Nancy (born 1940) French philosopher.
David Lewis (1941–2001). Modal realism.
Joxe Azurmendi (born 1941). Basque Philosopher, Political philosophy, Social philosophy, Philosophy of language
Derek Parfit (1942-2017).
Giorgio Agamben (born 1942). state of exception, form-of-life, homo sacer, and the concept of biopolitics
Gayatri Chakravorty Spivak (born 1942). Post-colonialism, Feminism, Literary theory
Peter Singer (born 1946) Moral philosopher on animal liberation, effective altruism
John Ralston Saul (born 1947).
Slavoj Žižek (born 1949). Hegelianism, Marxism and Lacanian psychoanalysis
Ken Wilber (born 1949). Integral Theory.
Cornel West (born 1953).
Judith Butler (born 1956). Poststructuralist, feminist, queer theory
Alexander Wendt (born 1958). Social constructivist
"""

greeksWithDates = greeksWithDates.splitlines()
greeksWithPeriods = greeksWithPeriods.splitlines()
hellenisticEra = hellenisticEra.splitlines()
romanEra = romanEra.splitlines()
medievalWithDates = medievalWithDates.splitlines()
medievalWithPeriods = medievalWithPeriods.splitlines()
earlyModernWithDates = earlyModernWithDates.splitlines()
earlyModernWithPeriods = earlyModernWithPeriods.splitlines()
modernEra = modernEra.splitlines()

listtest2 = [greeksWithDates,
greeksWithPeriods,
hellenisticEra,
romanEra,
medievalWithDates,
medievalWithPeriods,
earlyModernWithDates,
earlyModernWithPeriods,
modernEra]

# listtest2 = [len(greeksWithDates),
# len(greeksWithPeriods),
# len(hellenisticEra),
# len(romanEra),
# len(medievalWithDates),
# len(medievalWithPeriods),
# len(earlyModernWithDates),
# len(earlyModernWithPeriods),
# len(modernEra)]
# print listtest2

# eras = ["Greek,",
# "Greek,",
# "Hellenistic,",
# "Roman,",
# "Medieval,",
# "Medieval,",
# "Early Modern,",
# "Early Modern,",
# "Modern,",]
eras = ["Greek,",
"Hellenistic,",
"Roman,",
"Medieval,",
"Early Modern,",
"Modern,",]

philosophers = ["Thales of Miletus","Pherecydes of Syros","Anaximander","Anaximenes of Miletus","Pythagoras","Xenophanes","Epicharmus of Kos","Heraclitus","Parmenides","Anaxagoras","Empedocles","Zeno of Elea","Protagoras","Sophistic works of Antiphon","Hippias","Gorgias","Socrates","Critias","Prodicus","Leucippus","Thrasymachus","Democritus","Diagoras of Melos","Antisthenes","Aristippus","Alcidamas","Lycophron (sophist)","Diogenes of Apollonia","Hippo (philosopher)","Xenophon","Plato","Speusippus","Eudoxus of Cnidus","Diogenes","Xenocrates","Aristotle","Archelaus (philosopher)","Melissus of Samos","Cratylus","Ion of Chios","Echecrates","Timaeus of Locri","Theophrastus","Pyrrho","Strato of Lampsacus","Epicurus","Zeno of Citium","Timon of Phlius","Chrysippus","Carneades","Lucretius","Cicero","Philo","Seneca the Younger","Epictetus","Marcus Aurelius","Sextus Empiricus","Plotinus","Porphyry (philosopher)","Iamblichus","Augustine of Hippo","Proclus","Boethius","John Philoponus","Al-Kindi","John Scotus Eriugena","Al-Faràbi","Saadia Gaon","Al-Razi","Avicenna","Solomon ibn Gabirol","Anselm of Canterbury","Al-Ghazali","Peter Abelard","Abraham ibn Daud","Peter Lombard","Averroes","Maimonides","Francis of Assisi","Robert Grosseteste","Albertus Magnus","Roger Bacon","Thomas Aquinas","Bonaventure","Siger of Brabant","Ramon Llull","Meister Eckhart","Duns Scotus","Marsilius of Padua","William of Ockham","Gersonides","Jean Buridan","John Wycliffe","Nicole Oresme","Hasdai Crescas","Gemistus Pletho","Nicholas of Cusa","Lorenzo Valla","Marsilio Ficino","Giovanni Pico della Mirandola","Boetius of Dacia","Erasmus","Niccolò Machiavelli","Thomas More","Martin Luther","Petrus Ramus","John Calvin","Michel de Montaigne","Pierre Charron","Giordano Bruno","Francisco Suarez","Francis Bacon","Galileo Galilei","Hugo Grotius","François de La Mothe Le Vayer","Marin Mersenne","Robert Filmer","Pierre Gassendi","René Descartes","Baltasar Gracián","Thomas Hobbes","Antoine Arnauld","Henry More","Jacques Rohault","Ralph Cudworth","Blaise Pascal","Margaret Cavendish, Duchess of Newcastle-upon-Tyne","Arnold Geulincx","Pierre Nicole","Géraud de Cordemoy","Robert Boyle","Anne Conway (philosopher)","Richard Cumberland (philosopher)","Baruch Spinoza","Samuel von Pufendorf","John Locke","Joseph Glanvill","Nicolas Malebranche","Isaac Newton","Simon Foucher","Pierre Bayle","Damaris Cudworth Masham","John Toland","Gottfried Wilhelm Leibniz","John Norris (philosopher)","Jean Meslier","Giambattista Vico","Bernard Mandeville","Anthony Ashley-Cooper, 3rd Earl of Shaftesbury","Samuel Clarke","Catherine Trotter Cockburn","Christian Wolff (philosopher)","George Berkeley","Montesquieu","Joseph Butler","Francis Hutcheson (philosopher)","John Gay (philosopher)","David Hartley (philosopher)","Julien Offray de La Mettrie","Voltaire","Thomas Reid","David Hume","Jean-Jacques Rousseau","Denis Diderot","Alexander Gottlieb Baumgarten","Claude Adrien Helvétius","Étienne Bonnot de Condillac","Jean le Rond d'Alembert","Baron d'Holbach","Adam Smith","Richard Price","Immanuel Kant","Moses Mendelssohn","Gotthold Ephraim Lessing","Edmund Burke","William Paley","Thomas Jefferson","Jeremy Bentham","Sylvain Maréchal","Dugald Stewart","William Godwin","Mary Wollstonecraft","Friedrich Schiller","Johann Gottlieb Fichte","Edward Herbert, 1st Baron Herbert of Cherbury","Jean-Baptiste Lamarck","Pierre-Simon Laplace","Joseph de Maistre","Claude Henri de Rouvroy, comte de Saint-Simon","Germaine de Staël","Friedrich Schleiermacher","Georg Wilhelm Friedrich Hegel","James Mill","Friedrich Wilhelm Joseph Schelling","Bernard Bolzano","Richard Whately","Arthur Schopenhauer","John Austin (legal philosopher)","William Whewell","Auguste Comte","Ralph Waldo Emerson","Ludwig Feuerbach","Alexis de Tocqueville","Max Stirner","Augustus De Morgan","John Stuart Mill","Pierre-Joseph Proudhon","Charles Darwin","Margaret Fuller","Søren Kierkegaard","Henry David Thoreau","Sir William Hamilton, 9th Baronet","Sojourner Truth","Harriet Taylor Mill","Mikhail Bakunin","Elizabeth Cady Stanton","Hermann Lotze","Karl Marx","Friedrich Engels","Herbert Spencer","Susan B. Anthony","Wilhelm Dilthey","Edward Caird","Thomas Hill Green","Henry Sidgwick","Ernst Mach","Franz Brentano","Charles Sanders Peirce","William James","Peter Kropotkin","Friedrich Nietzsche","William Kingdon Clifford","F.H. Bradley","Vilfredo Pareto","Bernard Bosanquet (philosopher)","Gottlob Frege","John Cook Wilson","Hans Vaihinger","David George Ritchie","Alexius Meinong","Henri Poincaré","Josiah Royce","Andrew Seth Pringle-Pattison","Ferdinand de Saussure","Émile Durkheim","Giuseppe Peano","Edmund Husserl","Samuel Alexander","Henri Bergson","John Dewey","Jane Addams","Pierre Duhem","Karl Groos","Alfred North Whitehead","George Herbert Mead","Max Weber","Miguel de Unamuno","J. M. E. McTaggart","Benedetto Croce","Emma Goldman","Rosa Luxemburg","G.E. Moore","Martin Buber","George Santayana","Harold Arthur Prichard","Bertrand Russell","Arthur Oncken Lovejoy","Nikolai Berdyaev","Ernst Cassirer","Max Scheler","Giovanni Gentile","Ralph Barton Perry","W.D. Ross","Pierre Teilhard de Chardin","Hans Kelsen","Moritz Schlick","Otto Neurath","Nicolai Hartmann","Jacques Maritain","José Ortega y Gasset","Clarence Irving Lewis","Gaston Bachelard","Georg Lukács","Walter Terence Stace","Karl Barth","C. D. Broad","Ludwig Wittgenstein","Gabriel Marcel","Martin Heidegger","Antonio Gramsci","Rudolf Carnap","Walter Benjamin","Brand Blanshard","F. S. C. Northrop","Roman Ingarden","Susanne Langer","Friedrich Waismann","Georges Bataille","Herbert Marcuse","Xavier Zubiri","Leo Strauss","H.H. Price","Gilbert Ryle","Hans-Georg Gadamer","Jacques Lacan","Alfred Tarski","Ernest Nagel","Karl Popper","Mortimer J. Adler","Frank P. Ramsey","Theodor W. Adorno","Ernest Addison Moody","Jean-Paul Sartre","Karl Jaspers","Eugen Fink","Ayn Rand","Kurt Gödel","Emmanuel Levinas","Hannah Arendt","H.L.A. Hart","Charles Stevenson","Maurice Merleau-Ponty","Simone de Beauvoir","Willard van Orman Quine","Simone Weil","A.J. Ayer","J.L. Austin","Marshall McLuhan","Alan Turing","Wilfrid Sellars","Albert Camus","Paul Ricœur","Roland Barthes","J. L. Mackie","Donald Davidson (philosopher)","Louis Althusser","R. M. Hare","P. F. Strawson","John Rawls","Zygmunt Bauman","Frantz Fanon","Gilles Deleuze","Michel Foucault","Hilary Putnam","David Malet Armstrong","John Howard Yoder","Noam Chomsky","Bernard Williams","Jean Baudrillard","Jürgen Habermas","Jaakko Hintikka","Alasdair MacIntyre","Allan Bloom","Pierre Bourdieu","Jacques Derrida","Guy Debord","Richard Rorty","Charles Taylor (philosopher)","John Searle","Alvin Plantinga","Jerry Fodor","Robert M. Pirsig","Thomas Nagel","Alain Badiou","Robert Nozick","Tom Regan","Saul Kripke","Jean-Luc Nancy","David Lewis (philosopher)","Joxe Azurmendi","Derek Parfit","Giorgio Agamben","Gayatri Chakravorty Spivak","Peter Singer","John Ralston Saul","Slavoj Žižek","Ken Wilber","Cornel West","Judith Butler","Alexander Wendt"]

# can get the names from wikipedia timeline list
# now i need to use names to get info box info...then start writing to csv
# and then will need to know how to generate node/link csv files and influences/influenced
f = open('compiledSummaryInfo.csv', 'w')
f.write("phil_id," + "name," + "era," + "summary," + '\n')

count = 0
#getting the roman era philosophers
for y in range(0, 41):
    f.write(str(y) + ",")
    name=""
    name = philosophers[y].encode('utf-8')
    f.write("\"" + name.encode('utf-8') + "\"" + ",")
    # print("\"" + name + "\"" + ",")

    f.write(eras[count] +",")
    try:
        f.write("\"" + "\"" + "\"" + wikipedia.summary(name).replace('"', "'")  + "\"" + "\"" + "\"" + "\n")
    except:
        f.write("\"" + "\"" + "\"" "\"" + "\"" + "\"" + "\n")

#getting the hellenistic era philosophers
count += 1
for y in range(42, 49):
    f.write(str(y) + ",")
    name=""
    name = philosophers[y].encode('utf-8')
    f.write("\"" + name.encode('utf-8') + "\"" + ",")
    # print("\"" + name + "\"" + ",")

    f.write(eras[count] +",")

    try:
        f.write("\"" + "\"" + "\"" + wikipedia.summary(name).replace('"', "'").encode('utf-8')  + "\"" + "\"" + "\"" + "\n")
    except:
        f.write("\"" + "\"" + "\"" "\"" + "\"" + "\"" + "\n")

#getting the roman era philosophers
count += 1
for y in range(50, 61):
    f.write(str(y) + ",")
    name=""
    name = philosophers[y].encode('utf-8')
    f.write("\"" + name.encode('utf-8') + "\"" + ",")
    # print("\"" + name + "\"" + ",")

    f.write(eras[count] +",")

    try:
        f.write("\"" + "\"" + "\"" + wikipedia.summary(name).replace('"', "'").encode('utf-8')  + "\"" + "\"" + "\"" + "\n")
    except:
        f.write("\"" + "\"" + "\"" "\"" + "\"" + "\"" + "\n")

#getting the medieval era philosophers
count += 1
for y in range(62, 100):
    f.write(str(y) + ",")
    name=""
    name = philosophers[y].encode('utf-8')
    f.write("\"" + name.encode('utf-8') + "\"" + ",")
    # print("\"" + name + "\"" + ",")

    f.write(eras[count] +",")

    try:
        f.write("\"" + "\"" + "\"" + wikipedia.summary(name).replace('"', "'").encode('utf-8')  + "\"" + "\"" + "\"" + "\n")
    except:
        f.write("\"" + "\"" + "\"" "\"" + "\"" + "\"" + "\n")

#getting the early modern era philosophers
count += 1
for y in range(101, 184):
    f.write(str(y) + ",")
    name=""
    name = philosophers[y].encode('utf-8')
    f.write("\"" + name.encode('utf-8') + "\"" + ",")
    # print("\"" + name + "\"" + ",")

    f.write(eras[count] +",")

    try:
        f.write("\"" + "\"" + "\"" + wikipedia.summary(name).replace('"', "'").encode('utf-8')  + "\"" + "\"" + "\"" + "\n")
    except:
        f.write("\"" + "\"" + "\"" "\"" + "\"" + "\"" + "\n")

#getting the modern era philosophers
count += 1
for y in range(185, 380):
    f.write(str(y) + ",")
    name=""
    name = philosophers[y].encode('utf-8')
    f.write("\"" + name.encode('utf-8') + "\"" + ",")
    # print("\"" + name + "\"" + ",")

    f.write(eras[count] +",")

    try:
        f.write("\"" + "\"" + "\"" + wikipedia.summary(name).replace('"', "'").encode('utf-8')  + "\"" + "\"" + "\"" + "\n")
    except:
        f.write("\"" + "\"" + "\"" "\"" + "\"" + "\"" + "\n")

# f.write("Name," + "Era," + "Region," + "School_Tradition," + "Influenced," + "Influences," + "Main_Interests," + "Notable_Ideas," + "Date_Of_Birth," + "Date_Of_Death," + "Summary," + '\n')
# for x in range(0, len(eras)):
#     for y in range(0, len(listtest2[x])):
#         name=""
#         if x == 1 or x == 5 or x == 7:
#             # do stuff with periods
#             end = listtest2[x][y].find(".")
#             # print listtest2[x][y][0:end] + "," + eras[x]
#             name = listtest2[x][y][0:end].encode('utf-8')
#             f.write("\"" + name + "\"" + ",")
#             # print("\"" + name + "\"" + ",")
#
#         else:
#             # do stuff with dates/parentheses
#             end = listtest2[x][y].find("(") - 1
#             # print listtest2[x][y][0:end] + "," + eras[x]
#             name = listtest2[x][y][0:end].encode('utf-8')
#             f.write("\"" + name + "\"" + ",")
#             # print("\"" + name + "\"" + ",")
#
#         f.write(eras[x] +",")
#         f.write("\"" + "\"" + "\"" + wikipedia.summary(name).replace('"', "'").encode('utf-8')  + "\"" + "\"" + "\"" + "\n")
        # if error, just leave the thing none
        # page = wptools.page(name)
        # try:
        #     region = page.get_parse().infobox["region"]
        # except KeyError:
        #     region = ""
        # except TypeError:
        #     region = ""
        # try:
        #     school_tradition = page.get_parse().infobox["school_tradition"]
        # except KeyError:
        #     school_tradition = ""
        # except TypeError:
        #     school_tradition = ""
        # try:
        #     influenced = page.get_parse().infobox["influenced"]
        # except KeyError:
        #     influenced = ""
        # except TypeError:
        #     influenced = ""
        # try:
        #     influences = page.get_parse().infobox["influences"]
        # except KeyError:
        #     influences = ""
        # except TypeError:
        #     influences = ""
        # try:
        #     main_interests = page.get_parse().infobox["main_interests"]
        # except KeyError:
        #     main_interests = ""
        # except TypeError:
        #     main_interests = ""
        # try:
        #     notable_ideas = page.get_parse().infobox["notable_ideas"]
        # except KeyError:
        #     notable_ideas = ""
        # except TypeError:
        #     notable_ideas = ""
        # try:
        #     birth_date = page.get_parse().infobox["birth_date"]
        # except KeyError:
        #     birth_date = ""
        # except TypeError:
        #     birth_date = ""
        # try:
        #     death_date = page.get_parse().infobox["death_date"]
        # except KeyError:
        #     death_date = ""
        # except TypeError:
        #     death_date = ""
        # try:
        #     summary = "\"" + "\"" + "\"" + wikipedia.page(title=name).summary.encode('utf-8') +  "\"" + "\"" + "\"" + '\n'
        # except KeyError:
        #     summary = ""
        # except TypeError:
        #     summary = ""

        # try:
        #     notable_ideas = page.get_parse().infobox["notable_ideas"]
        # except KeyError:
        #     print "KeyError"
        # except TypeError:
        #     print "TypeError"

        # try:
        #     #getting info box data with wptools
        #     print page.get_parse().infobox
        #
        #     #getting summary data with wikipedia tool
        #     print type(summary)
        #     print wikipedia.summary(name)
        # except KeyError:
        #     print "KeyError"
        # except TypeError:
        #     print "TypeError"

        # listing = [region, school_tradition, influenced, influences, main_interests, notable_ideas, birth_date, death_date, summary]
        # newLine = ""
        #
        # for x in range(0,len(listing)):
        #     # newLine = newLine + re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', listing[x]).replace(" ", "") + ","
        #     if (x is (len(listing)-1)):
        #         f.write(summary)
        #         # f.write(wikipedia.summary(name) + ",")
        #     else:
        #         newLine = "\"" + "\"" + "\"" + re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', listing[x]) + "\"" + "\"" + "\"" + ","
        #         newLine = newLine.encode('utf-8')
        #         # print newLine
        #         f.write(newLine)

f.close()
