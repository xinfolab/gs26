myApp = angular.module('myApp', ['ngRoute']).factory('AuthService',
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
    .then(function (data, status) {
      if(status === 200 && data.result){
        user = true;
        deferred.resolve();
      } else {
        user = false;
        deferred.reject();
      }
    },
    // handle error
    function (data) {
      user = false;
      deferred.reject();
    });

  // return promise object
  return deferred.promise;

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

function register(email, password) {

  // create a new instance of deferred
  var deferred = $q.defer();

  // send a post request to the server
  $http.post('/api/register', {email: email, password: password})
    // handle success
    .then(function (data, status) {
      if(status === 200 && data.result){
        deferred.resolve();
      } else {
        deferred.reject();
      }
    },
    // handle error
    function (data) {
      deferred.reject();
    });

  // return promise object
  return deferred.promise;

}

function isLoggedIn() {
  if(user) {
    return true;
  } else {
    return false;
  }
}



    // return available functions for use in controllers
    return ({
      isLoggedIn: isLoggedIn,
      login: login,
      logout: logout,
      register: register
    });

}]);