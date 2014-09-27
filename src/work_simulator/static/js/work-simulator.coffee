
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
