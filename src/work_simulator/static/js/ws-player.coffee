app = angular.module 'wsPlayer', ['ngResource']

app.controller 'PlayerController', ['$scope', '$location', 'Player', ($scope, $location, Player)->
  $scope.login = () ->
    Player.loggedIn = true

    if Player.loggedIn
      $location.path('/')

  $scope.logout = () ->
    Player.loggedIn = false
    Player.name = ''

  $scope.player = Player
]

app.factory 'Player', ['$resource', ($resource) ->
  {
    loggedIn: false,
    resource:   $resource('player/:playerId')
  }
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