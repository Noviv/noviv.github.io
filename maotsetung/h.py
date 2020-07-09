import os

d = {

1: "The Communist Party	The Chinese Communist Party is the core of the Chinese revolution, and its principles are based on Marxism–Leninism. Party criticism should be carried out within the Party.",
2: "Classes and Class Struggle	The revolution, and the recognition of class and class struggle, are necessary for peasants and the Chinese people to overcome both domestic and foreign enemy elements. This is not a simple, clean, or quick struggle.",
3: "Socialism and Communism	Socialism must be developed in China, and the route toward such an end is a democratic revolution, which will enable socialist and communist consolidation over a length of time. It is also important to unite with the middle peasants, and educate them on the failings of capitalism.",
4: "The Correct Handling of Contradictions Among the People	There are at least two basic kinds of contradiction: the antagonistic contradictions which exist between communist countries and their capitalist neighbors and between the people and the enemies of the people, and the contradictions among the people themselves, people unconvinced of China's new path, which should be dealt with in a democratic and non-antagonistic fashion.",
5: "War and Peace	War is a continuation of politics, and there are at least two types: just (progressive) and unjust wars, which only serve bourgeois interests. While no one likes war, we must remain ready to wage just wars against imperialist agitations.",
6: "Imperialism and All Reactionaries Are Paper Tigers	U.S. imperialism, and European and domestic reactionary forces, represent real dangers, and in this respect are like real tigers. However, because the goal of Chinese communism is just, and reactionary interests are self-centered and unjust, after struggle, they will be revealed to be much less dangerous than they were earlier perceived to be.",
7: "Dare to Struggle and Dare to Win	Fighting is unpleasant, and the people of China would prefer not to do it at all. At the same time, they stand ready to wage a just struggle of self-preservation against reactionary elements, both foreign and domestic.",
8: "People's War	China's masses are the greatest conceivable weapon for fighting against Japanese imperialism and domestic reactionaries. Basic strategic points for war against the Kuomintang are also enumerated.",
9: "The People's Army	The People's Army is not merely an organ for fighting; it is also an organ for the political advancement of the Party, as well as of production.",
10: "Leadership of Party Committees	Internal life of the Party is discussed. Committees are useful to avoid monopolization by others, and Party members must demonstrate honesty, openness in discussing problems, and the ability to learn and multitask.",
11: "The Mass Line	The mass line represents the creative and productive energies of the masses of the Chinese population, which are potentially inexhaustible. Party members should take their cue from the masses, and reinterpret policy with respect to the benefit of the masses.",
12: "Political Work	It is necessary for intellectuals, students, soldiers and the average peasant to pay attention and involve themselves with political work. This is particularly true in wartime.",
13: "Relations Between Officers and Men	Non-antagonistic and democratic relations between officers and men make for a stronger army.",
14: "Relations Between the Army and the People	An army that is cherished and respected by the people, and vice versa, is a nearly invincible force. The army and the people must unite on the grounds of basic respect.",
15: "Democracy in the Three Main Fields	Democracy and honesty play roles in the reform of the army, as well as in the life of the Party, and of cadres. \"Ultra-democracy\", which is defined as an individualistic bourgeois aversion to discipline, is to be avoided.",
16: "Education and the Training of Troops	Education must have a practical and political basis for the army, Party and cadres. Along democratic lines, it will also be possible for the officers to teach the soldiers, for the soldiers to teach the officers, and for the soldiers to teach each other.",
17: "Serving the People	It is the duty of the cadres and the Party to serve the people. Without the people's interests constantly at heart, their work is useless.",
18: "Patriotism and Internationalism	The patriotism of a communist nation and an internationalist sympathy for just struggles in other countries are in no way exclusive; on the contrary, they are linked deeply, as communism spreads throughout the world. At the same time, it is important for a country to retain modesty, and shun arrogance.",
19: "Revolutionary Heroism	The same limitless creative energy of the masses is also visible in the army, in their fighting style and indomitable will.",
20: "Building Our Country Through Diligence and Frugality	China's road to modernization will be built on the principles of diligence and frugality. Nor will it be legitimate to relax if, 50 years later, modernization is realized on a mass scale.",
21: "Self-Reliance and Arduous Struggle	It is necessary for China to become self-reliant in the course of the revolution, along the usual lines of class struggle. At the same time, it is a mistake for individuals to only see the good or the bad in a system, to the exclusion of all else.",
22: "Methods of Thinking and Methods of Work	Marxist dialectical materialism, which connotes the constant struggle between opposites in an empirical setting, is the best method toward constant improvement. Objective analysis of problems based on empirical results is at a premium.",
23: "Investigation and Study	It is necessary to investigate both the facts and the history of a problem in order to study and understand it.",
24: "Correcting Mistaken Ideas	Arrogance, lack of achievement after a prosperous period, selfishness, shirking work, and liberalism, are all evils to be avoided in China's development. Liberalism is taken to mean that one may avoid conflict or work in order to be more comfortable for the moment, while the problem continues to grow.",
25: "Unity	Unity of the masses, the Party and the whole country is essential. At the same time, criticism may take place along comradely lines, while at the same time a basic unity is felt and preserved. This is the dialectical method.",
26: "Discipline	Discipline is seen not to be exclusive to democratic methods. Basic points of military conduct are also enumerated.",
27: "Criticism and Self-Criticism	Criticism is a part of the Marxist dialectical method which is central to Party improvement; as such, communists must not fear it, but engage in it openly.",
28: "Communists	A communist must be selfless, with the interests of the masses at heart. He must also possess a largeness of mind, as well as a practical, far-sighted mindset.",
29: "Cadres	Cadres, the instrument for uniting with and working for the people, must be leaders versed in Marxist–Leninism. They must have both guidance and the freedom to use their creative inititave in solving problems. Newer cadres and older cadres must work together with a comradely respect, learning from each other.",
30: "Youth	The Chinese Youth represent an active, vital force in China, to be drawn upon. At the same time, it is necessary to educate them, and for the Youth League to give special attention to their problems and interests.",
31: "Women	Women represent a great productive force in China, and equality among the sexes is one of the goals of communism. The multiple burdens which women must shoulder are to be eased.",
32: "Culture and Art	Literature and art are discussed with respect to communism, in an orthodox fashion. (Principally consisting of quotations from \"Talks at the Yenan Forum on Literature and Art\".",
33: "Study	It is the responsibility of all to cultivate themselves, and study Marxism–Leninism deeply. It is also necessary for people to turn their attention to contemporary problems, along empirical lines."
}

for i in range(1, 34):
	f = open("Chapter{0}/{0}.txt".format(i), "w")
	f.write(d[i])
	f.close()
