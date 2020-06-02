import Vue from 'vue'
import Vuex from 'vuex'
import mqtt from "mqtt";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    direction: {
      up: "0",
      left: "0",
    },
    mqtt: {
      connected: false,
      client: "motorhemsidan",
      url: "mqtt://maqiatto.com",
      options: {
        port: 8883,
        clientId: "mqttjs_" +
          Math.random()
            .toString(16)
            .substr(2, 8),
        username: "jonathan.damsgaardfalck@abbindustrigymnasium.se",
        password: "jondriverbot",
      }
    }
  },
  mutations: {
    updateS(state,S){
      state.direction.up = S;
      state.direction.left = "0";
    },
    updateD(state,D){
      state.direction.left = D;
      state.direction.up = "0";
    },
    publishToMqtt(state, direction) {
      if (!state.mqtt.connected) { //Connects to MaQiaTTo online broker
        console.log("connecting");
        state.mqtt.client = mqtt.connect(state.mqtt.url, state.mqtt.options);
        console.log("connected?");
        state.mqtt.client
          .on("error", function (error) {
            console.log("Error...");
            state.mqtt.connected = false;
            console.log(state.mqtt.connected, error);
          })
          .on("close", function (error) {
            console.log("Closed... Disconnected", error);
            state.mqtt.connected = false;
          });
      }
      state.mqtt.connected = true;
      console.log("lr" + direction.left)
      console.log("fb" + direction.up)
      state.mqtt.client.publish("jonathan.damsgaardfalck@abbindustrigymnasium.se/driverbot", direction.left + "," + direction.up );
  },
  },
  actions: {
    atUpdateS: ({
      commit,
      state
    }, S) => {
      commit("updateS", S)
      commit("publishToMqtt", {
        up: state.direction.up,
        left: "0"
      });
    },
    atUpdateD: ({
      commit,
      state
    }, D) => {
      commit("updateD", D)
      commit("publishToMqtt", {
        left: state.direction.left,
        up: "0"
      });
    },
  },
  modules: {},
  getters: {
      direction: state => state.direction,
    }
})