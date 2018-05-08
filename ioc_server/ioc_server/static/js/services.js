myApp = angular.module('myApp', ['ngRoute']);
myApp.factory('AuthService',
  ['$q', '$timeout', '$http',
  function ($q, $timeout, $http) {

    // create user variable
    var user = null;

function login(email, password) {

  // create a new instance of deferred
  var deferred = $q.defer();

  // send a post request to the server
  $http.post('/api/login', {email: email, password: password})
    // handle success
    .then(function (response) {
      if(response.status === 200 && response.data['result']==true){
        user = true;
        deferred.resolve();
      } else {
        user = false;
        deferred.reject();
      }
    })
    // handle error
    .catch(function (data) {
      user = false;
      deferred.reject();
    });

  // return promise object
  return deferred.promise;

}

function register(email, username, password, password_confirm) {

  // create a new instance of deferred
  var deferred = $q.defer();

  // send a post request to the server
  $http.post('/api/register', {email: email, username: username, password: password, password_confirm: password_confirm})
    // handle success
    .then(function (response) {
      if(response.status === 200 && response.data['result']=='success'){
        deferred.resolve();
      } else {
        deferred.reject();
      }
    })
    // handle error
    .catch(function (response) {
      deferred.reject();
    });

  // return promise object
  return deferred.promise;

}

function isLoggedIn() {
  if(user) {
    $location.path('/login');
    return true;
  } else {
    return false;
  }
}

function logout() {

  // create a new instance of deferred
  var deferred = $q.defer();

  // send a get request to the server
  $http.get('/api/logout')
    // handle success
    .then(function (data) {
      user = false;
      deferred.resolve();
    },
    // handle error
    function (data) {
      user = false;
      deferred.reject();
    });

  // return promise object
  return deferred.promise;

}
    // return available functions for use in controllers
    return ({
      isLoggedIn: isLoggedIn,
      login: login,
      logout: logout,
      register: register
    });

}]);

