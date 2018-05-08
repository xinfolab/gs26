angular.module('myApp').controller('menuController',
  ['$scope', '$location',
  function ($scope, $location){
    var currentPath = $location.absUrl();

    $scope.menus = [{
      'name': 'dashboard',
      'url': 'dashboard',
      'class': 'design_app',
    },
    {
      'name': 'icons',
      'url': 'icons',
      'class': 'education_atom',
    },
    {
      'name': 'map',
      'url': 'map',
      'class': 'location_map-big',
    },
    {
      'name': 'notifications',
      'url': 'notifications',
      'class': 'ui-1_bell-53',
    },
    {
      'name': 'table list',
      'url': 'tables',
      'class': 'design_bullet-list-67',
    },
    {
      'name': 'typography',
      'url': 'typography',
      'class': 'text_caps-small',
    },
    {
      'name': 'registration',
      'url': 'signup#!/register',
      'class': 'users_single-02',
    },
    {
      'name': 'sign in',
      'url': 'signin#!/login',
      'class': 'users_single-02',
    }
    ];
    for(i=0; i<$scope.menus.length; i++){
      if(currentPath.includes($scope.menus[i].url))
        $scope.currentMenu = $scope.menus[i].name;
    }
    $scope.activeClass = function(pMenu){
      if(currentPath.includes(pMenu)){
        return "active";
      }
    }
  }]);

angular.module('myApp').controller('loginController',
  ['$scope', '$location', 'AuthService',
  function ($scope, $location, AuthService) {

    $scope.login = function () {

      // initial values
      $scope.error = false;
      $scope.disabled = true;

      // call login from service
      AuthService.login($scope.loginForm.email, $scope.loginForm.password)
        // handle success
        .then(function () {
          $scope.disabled = false;
          $scope.loginForm = {};
          location.reload();
        })
        // handle error
        .catch(function () {
          $scope.error = true;
          $scope.errorMessage = "Invalid username and/or password";
          $scope.disabled = false;
          $scope.loginForm = {};
        });

    };

}]);

angular.module('myApp').controller('registerController',
  ['$scope', '$location', 'AuthService',
  function ($scope, $location, AuthService) {

    $scope.register = function () {

      // initial values
      $scope.error = false;
      $scope.disabled = true;

      // call register from service
      AuthService.register($scope.registerForm.email,
        $scope.registerForm.username,
        $scope.registerForm.password,
        $scope.registerForm.password_confirm)
        // handle success
        .then(function () {
          $scope.error = false;
          $location.path('/login');
          $scope.disabled = false;
          $scope.registerForm = {};
          demo.regSuccess('top','center');
        })
        // handle error
        .catch(function () {
          $scope.error = true;
          $scope.errorMessage = "Something went wrong!";
          $scope.disabled = false;
          $scope.registerForm = {};
        });

    };

}]);

angular.module('myApp').controller('logoutController',
  ['$scope', '$location', 'AuthService',
  function ($scope, $location, AuthService) {

    $scope.logout = function () {
      // call logout from service
      AuthService.logout()
        .then(function () {
          $location.path('/login');
        });
    };

}]);