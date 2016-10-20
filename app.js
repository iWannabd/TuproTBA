var app = angular.module('tupro',[]);

app.controller('myCtrl',function($scope){
	
	var inputan = ['p','q','r','s',' '];
	var states = ['a','b'];
	var map = [
		//p   q   r   s   space
		['b','b','b','b',  'a'], //a
		['a','a','a','a',  'b']  //b
	];

	currstate = 'a';
	$scope.currState = currstate;

	$scope.reset = function(){
		currState = 'a';
		$scope.currState = 'a';
		$scope.asd = '';
		$scope.lastchar = '';
	}

	$scope.changeHandler = function(){
		var currchar = $scope.asd[$scope.asd.length-1];
		$scope.lastchar = currchar;
		
		indchar = inputan.indexOf(currchar);
		indstate = states.indexOf(currstate);

		currstate = map[indstate][indchar];

		$scope.currState = currstate;

	}
})