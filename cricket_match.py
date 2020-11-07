import random


def print_score(team, total_runs, wickets, overs):
	print(team + ' '+ str(total_runs)+'-'+ str(wickets) )
	print('overs' +' '+ str(overs))
	print()

def print_scorecard(scorecard):
	for score in scorecard:
		print(score)
	print()

def update_batting_scorecard(batsmen, scorecard, runs_scored=0, balls_faced=0, wicket_type=None, bowler= None):
	index = 0
	for i in range(len(scorecard)):
		if scorecard[i][0] == batsmen:
			break
		else:
			index += 1
	scorecard[i][1] += runs_scored
	scorecard[i][2] += balls_faced
	scorecard[i][3] =  wicket_type
	scorecard[i][4] =  bowler



# Match begins

teams = ['team1', 'team2']

# Toss
toss_winner = random.choice(teams)
toss_decision = random.choice(['bat', 'bowl'])
print(toss_winner + ' has won the toss and decided to '+toss_decision+' first.')

if toss_decision == 'bowl':
	if toss_winner == 'team1':
		innings1 = 'team2'
		innings2 = 'team1'
	else:
		innings1 = 'team1'
		innings2 = 'team2'
else:
	innings1 = toss_winner
	teams.remove(toss_winner)
	innings2 = teams[0]


print(innings1 +' will bat first.')

t1 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11']
t2 = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11']

if innings1 == 'team1':
	batsmen = t1
	bowlers = t2[6:]
else:
	batsmen = t2
	bowlers = t1[6:]

max_overs = 5
innings1_score = 0
wickets = 0
overs = 0
print_score(innings1, innings1_score, wickets, overs)

innings1_batting_scorecard = [['batsmen', 'runs scored', 'balls faced', 'wicket type', 'bowler']]
innings1_bowling_scorecard = [['bowler','overs','runs','wickets']]

batsmen1 = batsmen.pop(0)
batsmen2 = batsmen.pop(0)
innings1_batting_scorecard.append([batsmen1, 0, 0, None, None])
innings1_batting_scorecard.append([batsmen2, 0, 0, None, None])
on_strike = batsmen1

for over in range(max_overs):
	bowler = bowlers.pop(0)
	innings1_bowling_scorecard.append([bowler, 0, 0, 0])
	no_of_balls = 0
	
	while wickets < 10:
		delivery = random.choice(['legal', 'wide', 'no'])
				
		if delivery == 'legal':
			runs_scored = random.choice([0,1,2,3,4,6,'W'])
			no_of_balls += 1

			update_batting_scorecard(on_strike, innings1_batting_scorecard, balls_faced = 1)
			innings1_bowling_scorecard[over+1][1] = '0.'+str(no_of_balls)
			
			if no_of_balls == 6:
				overs = str(over+1)+'.0'
				innings1_bowling_scorecard[over+1][1] = '1.0'
			else:
				overs = str(over) + '.'+ str(no_of_balls)

		elif delivery == 'wide':
			runs_scored = random.choice([0,1,2,3,4,'W'])
			innings1_score += 1

			innings1_bowling_scorecard[over+1][2] += 1 
			print('wide')

		else:
			runs_scored = random.choice([0,1,2,3,4,6,'W'])
			innings1_score += 1
			
			innings1_bowling_scorecard[over+1][2] += 1 
			print('no ball')

		if runs_scored == 'W':
			wicket_types = ['bowled', 'catch out', 'run out', 'stumped', 'lbw', ]
			wickets += 1 
			
			if delivery == 'legal':
				wicket_type = random.choice(wicket_types)
			elif delivery == 'wide':
				wicket_type= random.choice(['stumped','run out'])
			else:
				wicket_type = 'run out'
			
			update_batting_scorecard(on_strike, innings1_batting_scorecard, wicket_type= wicket_type, bowler=bowler)
			innings1_bowling_scorecard[over+1][3] += 1 
			print(on_strike + ' was '+wicket_type+ ' by '+ bowler)

			if wickets < 10:
				if on_strike == batsmen1:
					if innings1 == 'team1':
						batsmen1 = t1.pop(0)
					else:
						batsmen1 = t2.pop(0)
					innings1_batting_scorecard.append([batsmen1, 0, 0, None, None])
					on_strike = batsmen1
				else:
					if innings1 == 'team1':
						batsmen2 = t1.pop(0)
					else:
						batsmen2 = t2.pop(0)
					innings1_batting_scorecard.append([batsmen2, 0, 0, None, None])
					on_strike = batsmen2
			if wicket_type == 'run out' and on_strike == batsmen1:
				on_strike = batsmen2
			elif wicket_type == 'run out' and on_strike == batsmen2:
				on_strike = batsmen1

		else:
			innings1_score += runs_scored
			if delivery != 'wide':
				update_batting_scorecard(on_strike, innings1_batting_scorecard, runs_scored = runs_scored)
			if runs_scored in [1,3]:
				if on_strike == batsmen1:
					on_strike = batsmen2
				else:
					on_strike = batsmen1
			innings1_bowling_scorecard[over+1][2] += runs_scored 
			print(str(runs_scored) + ' runs_scored')
		print_score(innings1, innings1_score, wickets, overs)
		
		if no_of_balls == 6:
			if on_strike == batsmen1:
				on_strike = batsmen2
			else:
				on_strike = batsmen1
			break
	print_scorecard(innings1_batting_scorecard)

print(innings1 +' batting scorecard')	
print_scorecard(innings1_batting_scorecard)
print(innings2 +' bowling scorecard')
print_scorecard(innings1_bowling_scorecard)



# Second Innings
t1 = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11']
t2 = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11']

print(innings2 +' will bat now.')

if innings2 == 'team1':
	batsmen = t1
	bowlers = t2[6:]
else:
	batsmen = t2
	bowlers = t1[6:]
max_overs = 5
innings2_score = 0
wickets = 0
overs = 0
print_score(innings2, innings2_score, wickets, overs)

innings2_batting_scorecard = [['batsmen', 'runs scored', 'balls faced', 'wicket type', 'bowler']]
innings2_bowling_scorecard = [['bowler','overs','runs','wickets']]


batsmen1 = batsmen.pop(0)
batsmen2 = batsmen.pop(0)
innings2_batting_scorecard.append([batsmen1, 0, 0, None, None])
innings2_batting_scorecard.append([batsmen2, 0, 0, None, None])
on_strike = batsmen1

for over in range(max_overs):
	bowler = bowlers.pop(0)
	innings2_bowling_scorecard.append([bowler, 0, 0, 0])
	no_of_balls = 0
	
	while wickets < 10 and innings2_score <= innings1_score:

		delivery = random.choice(['legal', 'wide', 'no'])
				
		if delivery == 'legal':
			runs_scored = random.choice([0,1,2,3,4,6,'W'])
			no_of_balls += 1
			update_batting_scorecard(on_strike, innings2_batting_scorecard, balls_faced = 1)
			innings2_bowling_scorecard[over+1][1] = '0.'+str(no_of_balls)
			if no_of_balls == 6:
				overs = str(over+1)+'.0'
				innings2_bowling_scorecard[over+1][1] = '1.0'
			else:
				overs = str(over) + '.'+ str(no_of_balls)

		elif delivery == 'wide':
			runs_scored = random.choice([0,1,2,3,4,'W'])
			innings2_score += 1
			innings2_bowling_scorecard[over+1][2] += 1 
			print('wide')
		else:
			runs_scored = random.choice([0,1,2,3,4,6,'W'])
			innings2_score += 1
			innings2_bowling_scorecard[over+1][2] += 1 
			print('no ball')
		if runs_scored == 'W':
			wicket_types = ['bowled', 'catch out', 'run out', 'stumped', 'lbw', ]
			wickets += 1 
			if delivery == 'legal':
				wicket_type = random.choice(wicket_types)
			elif delivery == 'wide':
				wicket_type= random.choice(['stumped','run out'])
			else:
				wicket_type = 'run out'
			update_batting_scorecard(on_strike, innings2_batting_scorecard, wicket_type= wicket_type, bowler=bowler)
			innings2_bowling_scorecard[over+1][3] += 1 
			print('wicket')

			if wickets < 10:
				if on_strike == batsmen1:
					if innings2 == 'team1':
						batsmen1 = t1.pop(0)
					else:
						batsmen1 = t2.pop(0)
					innings2_batting_scorecard.append([batsmen1, 0, 0, None, None])
					on_strike = batsmen1
				else:
					if innings2 == 'team1':
						batsmen2 = t1.pop(0)
					else:
						batsmen2 = t2.pop(0)
					innings2_batting_scorecard.append([batsmen2, 0, 0, None, None])
					on_strike = batsmen2
			if wicket_type == 'run out' and on_strike == batsmen1:
				on_strike = batsmen2
			elif wicket_type == 'run out' and on_strike == batsmen2:
				on_strike = batsmen1

		else:
			innings2_score += runs_scored
			if delivery != 'wide':
				update_batting_scorecard(on_strike, innings2_batting_scorecard, runs_scored = runs_scored)
			if runs_scored in [1,3]:
				if on_strike == batsmen1:
					on_strike = batsmen2
				else:
					on_strike = batsmen1
			innings2_bowling_scorecard[over+1][2] += runs_scored 
			print(str(runs_scored) + ' runs_scored')
		print_score(innings2, innings2_score, wickets, overs)
		
		if no_of_balls == 6:
			if on_strike == batsmen1:
				on_strike = batsmen2
			else:
				on_strike = batsmen1
			break
	print_scorecard(innings2_batting_scorecard)

print(innings2 +' batting scorecard')
print_scorecard(innings2_batting_scorecard)
print(innings1 +' bowling scorecard')
print_scorecard(innings2_bowling_scorecard)

if innings2_score > innings1_score:
	print(innings2+ ' has won the match by '+str(10-wickets)+' wickets')
elif innings1_score > innings2_score:
	print(innings1 + ' has won the match by '+str(innings1_score-innings2_score) + ' runs')
else:
	print('match tied') 
