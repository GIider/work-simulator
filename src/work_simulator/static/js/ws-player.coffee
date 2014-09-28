app = angular.module 'wsPlayer', ['ngResource']

app.controller 'PlayerController', ['$scope', '$location', ($scope, $location)->
  player = {
    loggedIn: false
  }

  $scope.login = () ->
    player.loggedIn = true

    if player.loggedIn
      $location.path('/')

  $scope.logout = () ->
    player.loggedIn = false
    player.name = ''

  $scope.player = player
]

app.factory 'Player', ['$resource', ($resource) ->
  $resource('player/:playerId')
]

app.directive 'playerLogin', ->
  {
    restrict: 'E',
    templateUrl: 'static/partials/player/player-login.html'
  }

app.directive 'playerRegistration', ->
  {
    restrict: 'E',
    templateUrl: 'static/partials/player/player-registration.html'
  }

app.directive 'playerList', ->
  {
    restrict: 'E',
    templateUrl: 'static/partials/player/player-list.html'
  }