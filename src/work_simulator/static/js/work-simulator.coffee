
app = angular.module 'workSimulator', ['ngRoute']

app.config ['$routeProvider', ($routeProvider) ->
  $routeProvider
    .when('/registration', {
      templateUrl: 'static/partials/pages/registration.html'
    })
    .when('/login', {
      templateUrl: 'static/partials/pages/login.html'
    })
    .otherwise({
      templateUrl: 'static/partials/pages/index.html'
    })
]

app.controller 'PlayerController', ['$scope', '$http', '$location', ($scope, $http, $location)->
  player = {
    loggedIn: false
  }

  $scope.login = () ->
    # use $http to login player
    player.loggedIn = true

    if player.loggedIn
      $location.path('/')

  $scope.player = player
]
