import sessionManagerReducer, {
    logIn,
    logOut,
    signUp, makeInitialState
} from './sessionManagerSlice'

describe('session manager reducer', () => {
    
    it('should handle initial state', () => {
      const initialState = makeInitialState()
      expect(sessionManagerReducer(initialState, { type: 'unknown' })).toEqual(
          initialState
      );
    });

    it('should show login pending while thunk running', () => {

        const initialState = makeInitialState()
        const expectedState = makeInitialState()
        expectedState.logInState.loggingIn = true

        expect(sessionManagerReducer(initialState, {type: logIn.pending})).toEqual(
            expectedState
        );
    });

    it('should show sign up pending while thunk running', () => {


        const initialState = makeInitialState()
        const expectedState = makeInitialState()
        expectedState.createAccountState.creatingAccount = true


        expect(sessionManagerReducer(initialState, {type: signUp.pending})).toEqual(
            expectedState
        );
    });

    it('should show log in resolved when successful', () => {

        const initialState = makeInitialState()
        const expectedState = makeInitialState()

        expectedState.logInState.loggedIn = true
        expectedState.user.token = "testtoken"
        expectedState.logInState.loggingIn = false
        expectedState.user.username = "tempusername"

        initialState.user.token = ""
        initialState.user.username = "tempusername"
        initialState.logInState.loggedIn = false
        initialState.logInState.loggingIn = true
        

        const response = {
            "data": {
                "token": "testtoken"
            },
            "status": 200,
            "statusText": "OK",
        }


        expect(sessionManagerReducer(initialState, {type: logIn.fulfilled, payload: response})).toEqual(expectedState);
    });

    it('should not show failed after logging out of successful after failing', () => {

        const initialState = makeInitialState()
        const expectedState = makeInitialState()

        initialState.user.token = ""
        initialState.logInState.loggedIn = false
        initialState.logInState.loggingIn = false
        initialState.logInState.logInFailed = true

        expectedState.logInState.loggedIn = false
        expectedState.logInState.loggingIn = true
        expectedState.logInState.logInFailed = false

        

        const response = {
            "data": {
                "token": "testtoken"
            },
            "status": 200,
            "statusText": "OK",
        }


        expect(sessionManagerReducer(initialState, {type: logIn.pending, payload: response})).toEqual(expectedState);
    });

    it('should show log out when requested', () => {

        const initialState = makeInitialState()
        const expectedState = makeInitialState()

        initialState.logInState.loggedIn = true
        initialState.user.token = "testtoken"
        initialState.logInState.loggingIn = false
        initialState.user.username = "tempusername"

        expectedState.user.token = ""
        expectedState.user.username = ""
        expectedState.logInState.loggedIn = false
        expectedState.logInState.loggingIn = false
        


        expect(sessionManagerReducer(initialState, {type: logOut,})).toEqual(expectedState);
    });

    it('should not show logged in when failed', () => {

        const initialState = makeInitialState()
        const expectedState = makeInitialState()

        expectedState.logInState.loggedIn = false
        expectedState.user.token = ""
        expectedState.logInState.loggingIn = false
        expectedState.logInState.logInFailed = true
        expectedState.user.username = "tempusername"

        initialState.user.token = ""
        initialState.user.username = "tempusername"
        initialState.logInState.loggedIn = false
        initialState.logInState.loggingIn = true
        

        const response = {
            "data": {
                "token": "testtoken"
            },
            "status": 401,
            "statusText": "OK",
        }


        expect(sessionManagerReducer(initialState, {type: logIn.rejected})).toEqual(expectedState);
    });
});