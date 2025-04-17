import { io } from 'socket.io-client'

const state = {
  messages: [],
  connected: false,
  socket: null
}

const mutations = {
  SET_SOCKET(state, socket) {
    state.socket = socket
  },
  SET_CONNECTED(state, status) {
    state.connected = status
  },
  ADD_MESSAGE(state, message) {
    state.messages.push(message)
  },
  CLEAR_MESSAGES(state) {
    state.messages = []
  }
}

const actions = {
  connect({ commit, state, rootState }) {
    if (state.socket) return

    const socket = io(process.env.VUE_APP_WS_URL || 'ws://localhost:8000', {
      auth: {
        token: rootState.auth.token
      }
    })

    socket.on('connect', () => {
      commit('SET_CONNECTED', true)
    })

    socket.on('disconnect', () => {
      commit('SET_CONNECTED', false)
    })

    socket.on('message', (message) => {
      commit('ADD_MESSAGE', message)
    })

    commit('SET_SOCKET', socket)
  },

  disconnect({ commit, state }) {
    if (state.socket) {
      state.socket.disconnect()
      commit('SET_SOCKET', null)
      commit('SET_CONNECTED', false)
    }
  },

  sendMessage({ state }, message) {
    if (state.socket && state.connected) {
      state.socket.emit('message', message)
    }
  },

  async fetchHistory({ commit }) {
    try {
      const response = await axios.get('/api/chat/history')
      commit('CLEAR_MESSAGES')
      response.data.forEach(message => {
        commit('ADD_MESSAGE', message)
      })
    } catch (error) {
      console.error('Error fetching chat history:', error)
    }
  }
}

const getters = {
  messages: state => state.messages,
  isConnected: state => state.connected
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
} 