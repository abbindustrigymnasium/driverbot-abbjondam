<template>
  <div>
  <v-container class="mt-12" >
    
      <v-row class="mb-12 fill-height" align="start" justify="center" >
      <h1 class="font-weight-light">Controller</h1>
      </v-row>
    

    <v-row justify="center" class="align-center" style="height: 450px;">
    <v-col  cols="12" md="6" lg="3">
      <v-card  justify="center" class="ma-auto" style="width: 108px">
        <v-responsive :aspect-ratio="9/9">
        <v-row justify="center">
          <v-btn  @mousedown="knappnere('f')"  @mouseup="knappnere('o')"  icon>
            <v-icon> mdi-chevron-up</v-icon>
          </v-btn>
        </v-row>
        <v-row justify="center">
          <v-btn @mousedown="knappnere('v')"  @mouseup="knappnere('o')" icon>
            <v-icon> mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn disabled icon>
            <v-audio > </v-audio>
          <v-icon> mdi-car-back</v-icon>
          </v-btn>
          <v-btn justify="left" @mousedown="knappnere('h')"  @mouseup="knappnere('o')" icon>
            <v-icon> mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
        <v-row justify="center">
          <v-btn @mousedown="knappnere('b')"  @mouseup="knappnere('o')" icon>
            <v-icon> mdi-chevron-down</v-icon>
          </v-btn>
        </v-row>
        </v-responsive>
      </v-card>
      <v-text-field class="d-none d-md-block"  :value="key" placeholder="Alternative: Use WASD keys in this text field to control the car" :rules="rules" @input="_=>key=_"> </v-text-field>
      </v-col>
    </v-row>
  </v-container>
  </div>
</template>
<script>



export default {
   data() {
     return {
       knapp : "0",
       S: "0",
       D: "0",
       key: "",
       sists : "",
       rules: [
        value => (value && value.length <= 1)
       ]
     };
   },
  methods: {
    knappnere(input){
      this.knapp = input
      // this.updateS()
    },
    updateS() {
      if(this.knapp == "f"){
        this.S = "f"
        this.$store.dispatch("atUpdateS", this.S);}
      if(this.knapp == "b"){
        this.S = "b"
        this.$store.dispatch("atUpdateS", this.S);
     
      }
      
      },
     updateD() {
      if(this.knapp == "h"){
        this.D = "h"
        this.$store.dispatch("atUpdateD", this.D);}
      if(this.knapp == "v"){
        this.D = "v"
        this.$store.dispatch("atUpdateD", this.D);
      }
      },
      keyupdate(){
        this.sista = this.key[this.key.length -1]
        this.key = ""
        if(this.sista == "w"){
          this.S = "f"
          this.$store.dispatch("atUpdateS", this.S);
        }
        if(this.sista == "s"){
          this.S = "b"
          this.$store.dispatch("atUpdateS", this.S);
        }
        if(this.sista == "d"){
          this.D = "h"
          this.$store.dispatch("atUpdateD", this.D);
        }
        if(this.sista == "a"){
          this.D = "v"
          this.$store.dispatch("atUpdateD", this.D);
        }
        
      }
  
  },
  mounted: function () {
        this.$nextTick(function () {
            window.setInterval(() => {
                this.updateS(),
                this.keyupdate(),
                this.updateD();
            },100);
        })
    }


}
</script>