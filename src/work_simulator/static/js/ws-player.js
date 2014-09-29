// Generated by CoffeeScript 1.8.0
(function() {
  var app;

  app = angular.module('wsPlayer', ['ngResource']);

  app.controller('PlayerController', [
    '$scope', '$location', 'Player', function($scope, $location, Player) {
      $scope.login = function() {
        Player.loggedIn = true;
        if (Player.loggedIn) {
          return $location.path('/');
        }
      };
      $scope.logout = function() {
        Player.loggedIn = false;
        return Player.name = '';
      };
      return $scope.player = Player;
    }
  ]);

  app.factory('Player', [
    '$resource', function($resource) {
      return {
        loggedIn: false,
        resource: $resource('player/:playerId')
      };
    }
  ]);

  app.directive('playerLogin', function() {
    return {
      restrict: 'E',
      templateUrl: 'static/partials/player/player-login.html'
    };
  });

  app.directive('playerRegistration', function() {
    return {
      restrict: 'E',
      templateUrl: 'static/partials/player/player-registration.html'
    };
  });

  app.directive('playerList', function() {
    return {
      restrict: 'E',
      templateUrl: 'static/partials/player/player-list.html'
    };
  });

}).call(this);

//# sourceMappingURL=ws-player.js.map
