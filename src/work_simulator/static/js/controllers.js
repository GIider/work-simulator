var workSimulator = angular.module('workSimulator', []);

angular.module('workSimulator', ['ngResource'])
	.factory('Player', function($resource) {
		return $resource('/api/player/:id', {}, {
			query: {
				method: 'GET',
				params: { id: '' },
				isArray: true
			}
		});
	})
;


function PlayerListController($scope, Player) {
	var playerQuery = Player.get({}, function(players) {
		$scope.players = players.objects;
	});
}