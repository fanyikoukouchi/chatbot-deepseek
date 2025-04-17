import axios from 'axios'

const state = {
  token: localStorage.getItem('token') || '',
  isAuthenticated: !!localStorage.getItem('token'),
  user: null
}

const mutations = {
  SET_TOKEN(state, token) {
    state.token = token
    state.isAuthenticated = !!token
    if (token) {
      localStorage.setItem('token', token)
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    } else {
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authorization']
    }
  },
  SET_USER(state, user) {
    state.user = user
  }
}

const actions = {
  async login({ commit }, credentials) {
    try {
      const response = await axios.post('/api/auth/login', credentials)
      commit('SET_TOKEN', response.data.access_token)
      commit('SET_USER', response.data.user)
      return response.data
    } catch (error) {
      throw error
    }
  },
  
  async register({ commit }, userData) {
    try {
      const response = await axios.post('/api/auth/register', userData)
      commit('SET_TOKEN', response.data.access_token)
      commit('SET_USER', response.data.user)
      return response.data
    } catch (error) {
      throw error
    }
  },
  
  async logout({ commit }) {
    commit('SET_TOKEN', '')
    commit('SET_USER', null)
  },
  
  async fetchUser({ commit }) {
    try {
      const response = await axios.get('/api/auth/me')
      commit('SET_USER', response.data)
      return response.data
    } catch (error) {
      throw error
    }
  }
}

const getters = {
  isAuthenticated: state => state.isAuthenticated,
  currentUser: state => state.user
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
} 