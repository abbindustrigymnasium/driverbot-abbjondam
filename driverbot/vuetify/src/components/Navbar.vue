<template>
  <v-container>

    <v-app-bar flat clipped-left fixed class="grey darken-3">
        <!-- <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon> -->
        <v-toolbar-title class="text-uppercase grey--text">
            <span class="font-weight-light">Driverbot</span>
            <span>Controller</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn v-if="signin == false" text color="grey" @click="signin=true">
            <span >Sign In</span>
            <v-icon right>mdi-login</v-icon>
        </v-btn>
        <v-btn v-else-if="signin == true" text color="grey" @click="signin=false">
            <span >Sign Out</span>
            <v-icon right>mdi-logout</v-icon>
        </v-btn>
    </v-app-bar>

  
    <v-navigation-drawer  clipped :mini-variant="mini" permanent v-model="drawer" app class="grey darken-3 mt-7">   
    
        <v-list class="mt-6"> 
            
            <v-list-item  v-for="link in links" :key="link.text" router :to="link.route">
                <v-list-item-action class="grey--text">
                    <v-icon>{{link.icon}}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title class="grey--text">{{link.text}}</v-list-item-title>
                </v-list-item-content>
                
            </v-list-item>
            <v-list-item>
                <v-icon v-if="mini == true"  @click.stop="mini = !mini">mdi-chevron-right</v-icon>
                <v-icon v-if="mini == false"  @click.stop="mini = !mini">mdi-arrow-left</v-icon>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>

  </v-container>
</template>

<script>
export default {
    data(){

        return {
        drawer: false,
        mini: true,
        signin: false,
        links: [
         { icon: 'mdi-home', text: 'Home', route: '/' },
         { icon: 'mdi-google-controller', text: 'Controller', route: '/Controller' },
         { icon: 'mdi-cog', text: 'Settings', route: '/Settings' },
       ]
        }
    }

}
</script>

<style>

</style>
