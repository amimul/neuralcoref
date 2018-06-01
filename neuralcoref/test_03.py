# coding: utf8
import spacy, os, numpy, io
from spacy import util
from spacy.vectors import Vectors
from spacy.strings import StringStore
from neuralcoref.neuralcoref import NeuralCoref
nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('en_core_web_lg')
coref = NeuralCoref(nlp.vocab)
disk_model_path = os.getcwd() + '/spacy_model/en_coref_lg/neuralcoref'
coref.from_disk(disk_model_path)
text = """ = <unk> <unk> = 
 
 <unk> <unk> is a 2011 American black comedy film directed by Seth Gordon , written by Michael <unk> , John Francis <unk> and Jonathan Goldstein , based on a story by <unk> . It stars Jason Bateman , Charlie Day , Jason Sudeikis , Jennifer Aniston , Colin Farrell , Kevin Spacey , and Jamie <unk> . The plot follows three friends , played by Bateman , Day , and Sudeikis , who decide to murder their respective overbearing , abusive bosses , portrayed by Spacey , Aniston and Farrell . 
 <unk> 's script was bought by New Line Cinema in 2005 and the film spent six years in various states of pre @-@ production , with a variety of actors attached to different roles . By 2010 , Goldstein and <unk> had rewritten the script , and the film finally went into production . 
 The film premiered in Los Angeles on June 30 , 2011 , and received a wide release on July 8 , 2011 . The film exceeded financial expectations , <unk> over $ 28 million in the first three days , making it the number two film in the United States during its opening weekend , and going on to become the highest @-@ grossing black comedy film of all time in <unk> dollars , breaking the record previously set by The War of the Roses in 1990 . The film grossed over $ <unk> million worldwide during its theatrical run . 
 The film opened to positive critical reception , with several critics praising the ensemble cast , with each lead being singled out for their performances across reviews . The plot received a more mixed response ; some reviewers felt that its dark , humorous premise was explored well , while others felt the jokes were racist , <unk> , and <unk> . A sequel , <unk> <unk> 2 , was released on November 26 , 2014 . 
 
 = = Plot = = 
 
 Nick <unk> ( Bateman ) and Dale <unk> ( Day ) are friends who <unk> their bosses . Nick works at a financial firm for the sadistic David <unk> ( Spacey ) , who implies the possibility of a promotion for Nick for months , only to award it to himself . Dale is a <unk> assistant being sexually harassed by his boss , Dr. Julia Harris ( Aniston ) ; she threatens to tell his <unk> Stacy ( Lindsay <unk> ) that he had sex with her unless he actually has sex with her . Nick and Dale 's <unk> friend Kurt <unk> ( Sudeikis ) enjoys working for Jack <unk> ( Donald Sutherland ) at a chemical company , but after Jack unexpectedly dies of a heart attack , the company is taken over by Jack 's cocaine @-@ addicted son Bobby ( Farrell ) , whose apathy and incompetence threaten the future of the company . 
 At night , over drinks , Kurt <unk> suggests that their lives would be <unk> if their bosses were no longer around . Initially hesitant , they eventually agree to kill their employers . In search of a <unk> , the trio meet Dean " <unk> " Jones ( <unk> ) , an ex @-@ con who agrees to be their " murder consultant " . Jones suggests that Dale , Kurt and Nick kill each other 's bosses to hide their motive while making the deaths look like accidents . 
 The three <unk> Bobby 's house , and Kurt steals Bobby 's phone . They next go to <unk> 's house , where Kurt and Nick go inside while Dale <unk> in the car . <unk> returns home and confronts Dale for <unk> , but then has an allergy attack from the <unk> butter on the litter . Dale saves <unk> by stabbing him with an <unk> . Nick and Kurt think Dale is stabbing <unk> to death and flee , with Kurt accidentally dropping Bobby 's phone in <unk> 's bedroom . The next night , Kurt watches Julia 's home , but she <unk> and has sex with him . Nick and Dale <unk> wait outside Bobby 's and <unk> 's houses , respectively , to commit the murders , despite neither of them wanting to . <unk> discovers Bobby 's <unk> in his bedroom and uses it to find his address , <unk> his wife <unk> ( Julie Bowen ) is having an affair . He drives over and kills Bobby , with Nick as a secret witness . 
 Nick flees at high speed , setting off a traffic camera . The trio meet to discuss their reservations about continuing with their plan . They are arrested by the police , who believe the camera footage makes them suspects in Bobby 's murder . Lacking evidence , the police are forced to let the trio go free . The trio consult with Jones again , but learn that he never actually killed anyone , having been imprisoned for <unk> the film Snow Falling on <unk> . Jones suggests that they get <unk> to confess and secretly tape it . The three accidentally crash <unk> 's surprise birthday party , where Nick and Dale get <unk> to confess to the murder before realizing that Kurt , who has the audio recorder , is elsewhere having sex with <unk> . <unk> threatens to kill all three for attempting to blackmail him . They flee by car , but <unk> gives chase and repeatedly rams their vehicle . Believing they have committed a crime , the car 's navigation @-@ system operator <unk> <unk> Kurt 's car , allowing <unk> to catch and hold them at <unk> . <unk> shoots himself in the leg as he <unk> about his plan to frame them for murdering Bobby and attempting to kill him to get rid of the witness . 
 The police arrest Nick , Dale and Kurt , but the navigation @-@ system operator , Gregory , reveals that it is his companies policy to record all conversations for quality assurance . Gregory plays the tape that has <unk> <unk> he murdered <unk> . <unk> is sentenced to 25 years to life in prison , while the friends get their charges waived . Nick is promoted to president of the company under a sadistic CEO , Kurt retains his job under a new boss , and Dale blackmails Julia into ending her harassment by convincing her to sexually harass a supposedly unconscious patient , while Jones secretly records the act . 
 
 = = Cast = = 
 
 Jason Bateman as Nick <unk> 
 An executive at a financial firm who is manipulated into jumping through <unk> in order to get a promotion that his boss never intended to give him . <unk> wrote the role specifically for Bateman . 
 Charlie Day as Dale <unk> 
 A <unk> assistant who is sexually harassed by his boss . Described as a " <unk> romantic " in love with his fiancée . Ashton <unk> was in talks for the role at two different points in the lengthy production . Day was considered for the role following his co @-@ starring performance with Sudeikis in the 2010 film Going the <unk> — Reuters reported that industry <unk> believed his performance overshadowed the main stars . 
 Jason Sudeikis as Kurt <unk> 
 An account manager at a chemical company dealing with a new , drug @-@ addicted boss after his beloved former boss dies . Sudeikis was cast in May 2010 . 
 Jennifer Aniston as Dr. Julia Harris , <unk> 
 <unk> based the character on a former boss , claiming she was " very sexually aggressive with everybody " . When writing the script , <unk> intended for the role to go to Aniston . He stated , " but [ the aforementioned boss ] looked more like <unk> de <unk> . It was like flirting with a <unk> . So I decided for the sake of the movie , let ’ s go with Jennifer Aniston . ” The actress insisted on wearing a brown wig for the role , wanting to look different from other characters she had played . 
 Colin Farrell as Bobby <unk> 
 Described as a " <unk> <unk> " and a " corrupt and incompetent <unk> who 's in charge of things but clearly has no idea what he 's doing . " Farrell explained the motivation he gave to the character , stating " This guy thinks he 's God 's gift to women , God 's gift to <unk> , to humor , to the club scene , to everything . It 's all part of his grandiose sense of self @-@ esteem , which is probably <unk> a deeper sense of being a disappointment to his father and being riddled with envy over the relationship his father had with Kurt , and all kinds of other things . With <unk> , Seth gave me complete license to act as <unk> <unk> up as possible . " Farrell contributed significantly to the appearance of his character , suggesting the comb over hairstyle , pot @-@ belly and an affinity for Chinese <unk> . 
 Kevin Spacey as David <unk> 
 President of <unk> Industries . Tom Cruise , Philip Seymour Hoffman and Jeff Bridges had been approached by New Line Cinema to take the role , described as a <unk> master <unk> with an attractive wife . Spacey signed up for the role in June 2010 . The part was considered " integral " to the film . Gordon commented that the character was an amalgamation of several real bosses ( rather than one single person ) to avoid being sued . 
 Jamie <unk> as Dean " <unk> " Jones 
 The character had the more " colorful " name " <unk> Jones " , but it was changed at <unk> 's request , with producer Jay Stern commenting that <unk> felt it " was over the line " . The current name was said to be subject to further change , prior to the release of the film . <unk> contributed to his character 's appearance , suggesting full @-@ <unk> tattoos and a retro clothing style . <unk> described the appearance as " a guy who maybe went to jail for a minute and now he 's living in his own time capsule . When he got out he went right back to the clothes he thought were hot when he went in . " 
 During the six @-@ year development of the film , several actors were in negotiations to star , including Owen Wilson , Vince <unk> , Matthew <unk> , Ryan Reynolds , Dax Shepard , and Johnny <unk> . 
 Donald Sutherland portrays Jack <unk> , Bobby 's father and Kurt 's boss . On July 27 , 2010 , Isaiah <unk> was confirmed as joining the cast . <unk> was quoted as saying " It 's a smaller role " . He appears as Officer <unk> . Julie Bowen appears in the film as <unk> , <unk> 's wife . Bowen stated that her character " may or may not be a <unk> " , the character described as intentionally making her husband jealous . <unk> Gruffudd has a cameo as a male prostitute erroneously hired as a <unk> . Lindsay <unk> appears as Dale 's <unk> Stacy . P. J. <unk> plays Kenny <unk> , a former investment manager , now <unk> for drinks , while Wendell Pierce and Ron White play a pair of <unk> . Bob <unk> makes a cameo as sadistic <unk> CEO Louis Sherman . John Francis <unk> , a screenwriter on the film , cameos as Nick 's co @-@ worker Carter . 
 
 = = Production = = 
 
 
 = = = Development = = = 
 
 <unk> 's script for <unk> <unk> was sold at auction to New Line Cinema by <unk> 's production company Rat Entertainment in 2005 for a six @-@ figure amount . <unk> initially was interested in directing , but became occupied with directing the comedy Tower <unk> . Frank <unk> and David <unk> were in talks to direct . Jonathan Goldstein and John Francis <unk> rewrote the script in 2010 , and the project went into production with Seth Gordon directing . 
 
 = = = Design = = = 
 
 Production designer Shepherd <unk> specifically set out to create distinctly different environments for the three employees and their respective bosses ' homes and offices . Nick and <unk> 's workplace is the " <unk> " bullpen , which was designed to " enhance the discomfort and anxiety of lower @-@ level employees clustered in the center of the room where every movement is monitored by the boss from his corner office . " The design team met with financial <unk> and management companies to learn about the architecture of their office layouts to visually represent the experience of starting from a low @-@ ranking position in a <unk> and aspiring to an office . Costume designer Carol Ramsey worked with <unk> and set <unk> Jan <unk> to match <unk> 's suit to that of the surrounding " cold grey and blue " color palette of his office . <unk> 's home was described as " equally lacking in warmth " as the office but more lavishly decorated and " for show " , including an intentionally oversized portrait of him with his " trophy wife " . 
 <unk> Julia 's office was described as a " challenge " , <unk> a " sensual vibe " into a <unk> office . <unk> approached the design through Julia 's mentality , stating , " She 's a Type A professional at the top of her game , who likes to play cat @-@ and @-@ mouse , so it 's a completely controlled environment , with <unk> and views into other rooms so she always knows what 's going on " . " It 's highly designed , with rich <unk> and tones , <unk> artwork and subtle lighting — all very <unk> till you step into her private office . The <unk> close , the door locks and you think , ' It 's the Temple of Doom . ' " Similarly approaching the character 's home , the design allowed for wide windows which face onto a public street " which afford her the opportunity to put on the kind of show she couldn 't get away with at work . " 
 Bobby 's environments were designed with more contrast , the character being new to the work area . <unk> described the contrast as " the company reflects [ Jack <unk> 's ] human touch , whereas [ Bobby <unk> 's ] home is a <unk> shrine to himself and his <unk> <unk> . " <unk> continued , " It features a <unk> of anything he finds exotic and erotic , mostly Egyptian and Asian motifs with an ' 80s Studio 54 vibe , a makeshift <unk> , lots of mirrors and a <unk> table . " Some parts of the house design were provided by Farrell and Gordon 's interpretation of the character and his " infatuation " with martial arts and " his <unk> of prowess " . 
 
 = = = Filming = = = 
 
 Filming of <unk> <unk> took place in and around Los Angeles . The production team attempted to find locations " that people haven 't already seen a hundred times in movies and on TV " , aiming for the film to appear as if it could be taking place anywhere in America " where people are trying to pursue the American dream but getting stopped by a horrible boss . " " <unk> " was represented by an office building in <unk> , California , with the crew building the set on a vacant floor . For " <unk> Chemical " , the production team found a " perfect landscape of pipes and containers " in Santa Fe Springs , surrounding an unoccupied water cleaning and storage facility . To take advantage of the surrounding imagery , the warehouse required an extensive series of <unk> , including cutting windows into concrete walls and creating new <unk> to allow for visuals of the warehouse exterior and provide a setting for the final scene of Sutherland 's character . A <unk> Friday 's in Woodland Hills , Los Angeles , was used as a bar frequented by Nick , Dale , and Kurt , while the bar scene where they meet with Jones was staged in downtown Los Angeles . 
 The film was shot digitally using the <unk> Genesis camera . Gordon encouraged the actors to improvise , though Aniston claimed to not have taken advantage of the offer as much as her co @-@ stars , stating , " My dialogue was just so beautifully choreographed that there wasn ’ t much that I needed to do ” . 
 
 = = = Music = = = 
 
 The soundtrack was composed by award @-@ winning composer Christopher <unk> , with music contributed by Mike <unk> of Pearl Jam , Stefan <unk> of Dave Matthews Band and Money Mark — a collaborator with the <unk> Boys . <unk> , <unk> , and Mark worked with musicians Matt Chamberlain , David <unk> , Aaron Kaplan , Victor <unk> , Chris <unk> , <unk> <unk> and DJ <unk> to develop the music . Major contributions were provided by Mark on keyboard , <unk> and <unk> on guitar , <unk> and <unk> on bass , <unk> on drums and DJ <unk> on <unk> . 
 <unk> recorded the soundtrack at The Village recording studio in West Los Angeles and Capitol Records . <unk> attempted to remain " authentic " to the characters ' progression from average worker to calculated killer . To achieve this aim , he decided against recording digitally , instead recording the tracks on two @-@ inch analog tape , intending each musical cue to sound as if it was emanating from a vinyl record . He explained , " The idea was to put together a band that would record the score together the same way that they would make an album . It isn 't over @-@ produced or <unk> and digital in any way . It 's <unk> , noisy , and full of <unk> and <unk> . I knew that if we could <unk> some of this sonic magic in the score , then the <unk> and confidence of the music would play against Bateman , Sudeikis , and Charlie Day to really emphasize and elevate the humor in the situations that <unk> . " <unk> continued , " We tracked through tape before Pro Tools to get that fat sound , and made every choice based on feel rather than perfection . We even used the same <unk> that Money Mark played on Beck 's classic ‘ Where It 's At ’ . At the end of the day , Seth [ Gordon ] and I wanted to produce a score that is as <unk> and full of attitude as the movie itself . I think we did it ... and most of all , everyone had a blast in the process . " 
 <unk> <unk> : The Original Motion Picture Soundtrack was released in physical and digital formats on July 5 , 2011 , by <unk> Music . The soundtrack consists of 33 tracks with a <unk> of 63 minutes . 
"""

doc3 = nlp(text)
doc4 = coref(doc3)
