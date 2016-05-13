alldata = [('content', 13.1, 37.1, 8.7, 1.5),
('method', 10.6, 34.6, 13.4, 1.9),
('strelation', 27.1, 40.0, 2.9, 1.5),
('prrelation', 16.2, 37.8, 6.8, 0.8),
('equipment', 11.4, 29.8, 14.8, 4.9),
('enviroment', 12.2, 26.5, 14.9, 4.4),
('subject', 13.5, 29.7, 11.1, 2.4),
('school', 13.7, 37.6, 4.1, 1.2)]

def data():
    best=list()
    for i in range(0,len(alldata)):
        best.append(alldata[i][1])
    good=list()
    for i in range(0,len(alldata)):
        good.append(alldata[i][2])
    bad=list()
    for i in range(0,len(alldata)):
        bad.append(alldata[i][3])
    worst=list()
    for i in range(0,len(alldata)):
        worst.append(alldata[i][4])
    sumb=0
    for i in range(0,len(alldata)):
        sumb = sumb + best[i]
    sumg = 0
    for i in range(0,len(alldata)):
        sumg = sumg + good[i]
    goodsum = 0
    goodsum = sumb + sumg
    print "Best and Good sum ", goodsum
    average = 0
    gaverage = goodsum / len(alldata)
    print "Best & Good average ", gaverage

    sumb=0
    for i in range(0,len(alldata)):
        sumb = sumb + bad[i]
    sumw=0
    for i in range(0,len(alldata)):
        sumw = sumw + worst[i]
    badsum = 0
    badsum = sumb + sumw
    print "Worst & Bad sum", badsum

    baverage = 0
    baverage = badsum / len(alldata)
    print "Worst & Bad average", baverage
    
def lab10():
    data()
def main():
    lab10()
    raw_input()
if __name__=="__main__":
    main()

GW=list()
GW=["AMONG the vicissitudes incident to life no event could have filled me with greater anxieties than that of which the notification was transmitted by your order, and received on the 14th day of the present month. On the one hand, I was summoned by my country, whose voice I can never hear but with veneration and love, from a retreat which I had chosen with the fondest predilection, and, in my flattering hopes, with an immutable decision, as the asylum of my declining years - a retreat which was rendered every day more necessary as well as more dear to me by the addition of habit to inclination, and of frequent interruptions in my health to the gradual waste committed on it by time."
   ,"On the other hand, the magnitude and difficulty of the trust to which the voice of my country called me, being sufficient to awaken in the wisest and most experienced of her citizens a distrustful scrutiny into his qualifications, could not but overwhelm with despondence one who (inheriting inferior endowments from nature and unpracticed in the duties of civil administration) ought to be peculiarly conscious of his own deficiencies.",
   "In this conflict of emotions all I dare aver is that it has been my faithful study to collect my duty from a just appreciation of every circumstance by which it might be affected.",
   "All I dare hope is that if, in executing this task, I have been too much swayed by a grateful remembrance of former instances, or by an affectionate sensibility to this transcendent proof of the confidence of my fellow-citizens, and have thence too little consulted my incapacity as well as disinclination for the weighty and untried cares before me, my error will be palliated by the motives which mislead me, and its consequences be judged by my country with some share of the partiality in which they originated.",
   "Such being the impressions under which I have, in obedience to the public summons, repaired to the present station, it would be peculiarly improper to omit in this first official act my fervent supplications to that Almighty Being who rules over the universe, who presides in the councils of nations, and whose providential aids can supply every human defect, that His benediction may consecrate to the liberties and happiness of the people of the United States a Government instituted by themselves for these essential purposes, and may enable every instrument employed in its administration to execute with success the functions allotted to his charge.",
   "In tendering this homage to the Great Author of every public and private good, I assure myself that it expresses your sentiments not less than my own, nor those of my fellow-citizens at large less than either. ",
   " No people can be bound to acknowledge and adore the Invisible Hand which conducts the affairs of men more than those of the United States.",
   "Every step by which they have advanced to the character of an independent nation seems to have been distinguished by some token of providential agency; and in the important revolution just accomplished in the system of their united government the tranquil deliberations and voluntary consent of so many distinct communities from which the event has resulted can not be compared with the means by which most governments have been established without some return of pious gratitude, along with an humble anticipation of the future blessings which the past seem to presage.",
   "These reflections, arising out of the present crisis, have forced themselves too strongly on my mind to be suppressed.",
   "You will join with me, I trust, in thinking that there are none under the influence of which the proceedings of a new and free government can more auspiciously commence.",
   "By the article establishing the executive department it is made the duty of the President to recommend to your consideration such measures as he shall judge necessary and expedient.",
   "The circumstances under which I now meet you will acquit me from entering into that subject further than to refer to the great constitutional charter under which you are assembled, and which, in defining your powers, designates the objects to which your attention is to be given.",
   "It will be more consistent with those circumstances, and far more congenial with the feelings which actuate me, to substitute, in place of a recommendation of particular measures, the tribute that is due to the talents, the rectitude, and the patriotism which adorn the characters selected to devise and adopt them. ",
   "n these honorable qualifications I behold the surest pledges that as on one side no local prejudices or attachments, no separate views nor party animosities, will misdirect the comprehensive and equal eye which ought to watch over this great assemblage of communities and interests, so, on another, that the foundation of our national policy will be laid in the pure and immutable principles of private morality, and the preeminence of free government be exemplified by all the attributes which can win the affections of its citizens and command the respect of the world.",
   "I dwell on this prospect with every satisfaction which an ardent love for my country can inspire, since there is no truth more thoroughly established than that there exists in the economy and course of nature an indissoluble union between virtue and happiness; between duty and advantage; between the genuine maxims of an honest and magnanimous policy and the solid rewards of public prosperity and felicity; since we ought to be no less persuaded that the propitious smiles of Heaven can never be expected on a nation that disregards the eternal rules of order and right which Heaven itself has ordained; and since the preservation of the sacred fire of liberty and the destiny of the republican model of government are justly considered, perhaps, as deeply, as finally, staked on the experiment entrusted to the hands of the American people.",
   "Besides the ordinary objects submitted to your care, it will remain with your judgment to decide how far an exercise of the occasional power delegated by the fifth article of the Constitution is rendered expedient at the present juncture by the nature of objections which have been urged against the system, or by the degree of inquietude which has given birth to them. ",
   "Instead of undertaking particular recommendations on this subject, in which I could be guided by no lights derived from official opportunities, I shall again give way to my entire confidence in your discernment and pursuit of the public good; for I assure myself that whilst you carefully avoid every alteration which might endanger the benefits of an united and effective government, or which ought to await the future lessons of experience, a reverence for the characteristic rights of freemen and a regard for the public harmony will sufficiently influence your deliberations on the question how far the former can be impregnably fortified or the latter be safely and advantageously promoted.",
   "To the foregoing observations I have one to add, which will be most properly addressed to the House of Representatives.",
   "It concerns myself, and will therefore be as brief as possible. When I was first honored with a call into the service of my country, then on the eve of an arduous struggle for its liberties, the light in which I contemplated my duty required that I should renounce every pecuniary compensation.",
   "From this resolution I have in no instance departed; and being still under the impressions which produced it, I must decline as inapplicable to myself any share in the personal emoluments which may be indispensably included in a permanent provision for the executive department, and must accordingly pray that the pecuniary estimates for the station in which I am placed may during my continuance in it be limited to such actual expenditures as the public good may be thought to require.",
   "Having thus imparted to you my sentiments as they have been awakened by the occasion which brings us together, I shall take my present leave; but not without resorting once more to the benign Parent of the Human Race in humble supplication that, since He has been pleased to favor the American people with opportunities for deliberating in perfect tranquillity, and dispositions for deciding with unparalleled unanimity on a form of government for the security of their union and the advancement of their happiness, so His divine blessing may be equally conspicuous in the enlarged views, the temperate consultations, and the wise measures on which the success of this Government must depend."]

d=dict()
for i in range(0,len(GW)):
    for a in GW[i].split():
        if a in d:
            d[a]=d[a]+1
            print d
        else:
            d[a]=1
for a in d:
    if d[a]>=15:
        print a


President=list()
President=["There is a man here who has earned a lasting place in our hearts and in our history. President Reagan, on behalf of our Nation, I thank you for the wonderful things that you have done for America.",
   "I have just repeated word for word the oath taken by George Washington 200 years ago, and the Bible on which I placed my hand is the Bible on which he placed his.",
   "It is right that the memory of Washington be with us today, not only because this is our Bicentennial Inauguration, but because Washington remains the Father of our Country. ",
   " And he would, I think, be gladdened by this day; for today is the concrete expression of a stunning fact: our continuity these 200 years since our government began.",
   "We meet on democracy's front porch, a good place to talk as neighbors and as friends. For this is a day when our nation is made whole, when our differences, for a moment, are suspended.",
   "Heavenly Father, we bow our heads and thank You for Your love. Accept our thanks for the peace that yields this day and the shared faith that makes its continuance likely.",
   "Make us strong to do Your work, willing to heed and hear Your will, and write on our hearts these words: Use power to help people.",
   "For we are given power not to advance our own purposes, nor to make a great show in the world, nor a name.",
   "There is but one just use of power, and it is to serve people. Help us to remember it, Lord. Amen.",
   "I come before you and assume the Presidency at a moment rich with promise.",
   "We live in a peaceful, prosperous time, but we can make it better.",
   "For a new breeze is blowing, and a world refreshed by freedom seems reborn; for in man's heart, if not in fact, the day of the dictator is over.",
   "The totalitarian era is passing, its old ideas blown away like leaves from an ancient, lifeless tree.",
   "A new breeze is blowing, and a nation refreshed by freedom stands ready to push on.",
   "here is new ground to be broken, and new action to be taken. There are times when the future seems thick as a fog; you sit and wait, hoping the mists will lift and reveal the right path. ",
   "But this is a time when the future seems a door you can walk right through into a room called tomorrow.",
   "Great nations of the world are moving toward democracy through the door to freedom.",
   "Men and women of the world move toward free markets through the door to prosperity.",
   "he people of the world agitate for free expression and free thought through the door to the moral and intellectual satisfactions that only liberty allows.",
   "We know what works: Freedom works.",
   "We know what's right: Freedom is right. We know how to secure a more just and prosperous life for man on Earth: through free markets, free speech, free elections, and the exercise of free will unhampered by the state.",
   "For the first time in this century, for the first time in perhaps all history, man does not have to invent a system by which to live.",
   "We don't have to talk late into the night about which form of government is better. We don't have to wrest justice from the kings.",
   "We only have to summon it from within ourselves. We must act on what we know.",
   "I take as my guide the hope of a saint: In crucial things, unity; in important things, diversity; in all things, generosity.",
   "America today is a proud, free nation, decent and civil, a place we cannot help but love.",
   "We know in our hearts, not loudly and proudly, but as a simple fact, that this country has meaning beyond what we see, and that our strength is a force for good.",
   "But have we changed as a nation even in our time? Are we enthralled with material things, less appreciative of the nobility of work and sacrifice?",
   "My friends, we are not the sum of our possessions.",
   "hey are not the measure of our lives. In our hearts we know what matters.",
   "We cannot hope only to leave our children a bigger car, a bigger bank account. We must hope to give them a sense of what it means to be a loyal friend, a loving parent, a citizen who leaves his home, his neighborhood and town better than he found it. What do we want the men and women who work with us to say when we are no longer there?",
   "That we were more driven to succeed than anyone around us?",
   "Or that we stopped to ask if a sick child had gotten better, and stayed a moment there to trade a word of friendship?"]

c=dict()
for i in range(0,len(GB)):
    for b in GB[i].split():
        if b in c:
            c[b]=c[b]+1
            print c
        else:
            c[b]=1
for b in c:
    if c[b]>=10:
        print b