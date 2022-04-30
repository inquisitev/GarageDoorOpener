import sessionManagerReducer, {
    logIn,
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


        expect(sessionManagerReducer(initialState, {type: logIn.fulfilled, payload: response})).toEqual(expectedState);
    });
});