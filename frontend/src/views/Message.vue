<template lang="html">
    <div class="single-question mt-2">

        <div v-if="notFound" class="container">
            <h1 class="notFound">Messaggio non trovato!</h1>
        </div>
        <div v-else class="container">
            <h1>{{ message.content }}</h1>

            <MessageActions
                v-if="isOwner"
                :slug="slug"
            />

            <!-- <iframe> {{ message.cover }}</iframe> -->
            <span> {{ message.cover }}</span>

            <p class="mb-0">Messaggio aggiunto da</p>
                <span class="author_name">{{ message.author }}</span>
            </p>
            <p>{{ message.created_at }}</p>
            <hr>
            <!-- <template v-if="userHasAnswered">
              <p class="answer_added">Hai risposto a questo messaggio</p>
            </template> -->
            <template v-if="showForm">
              <form class="card" @submit.prevent="onSubmit">
                <div class="card-header px-3">
                  Aggiungi una risposta al messaggio
                </div>
                <div class="card-block">
                  <textarea
                    v-model="newAnswerBody"
                    classs="form-control"
                    placeholder="Aggiungi una risposta al messaggio"
                    rows="5"
                  ></textarea>
                </div>
                <div class="card-footer px-3">
                  <button type="submit" class="btn btn-sm btn-success">Aggiungi Risposta</button>
                </div>
              </form>
              <p class=" error mt-2">{{ error}}</p>
            </template>
            <template v-else>
              <button
                class="btn btn-sm btn-success"
                @click="showForm = true"
                >Rispondi al messaggio</button>
            </template>

            <hr>
            <AnswerComponent
              v-for="(answer, index) in answers"
              :answer="answer"
              :requestUser="requestUser"
              :key="index"
              @delete-answer="deleteAnswer"
            />
            <div class="my-4">
              <p v-show="loadingAnswers">...loading...</p>
              <button
                 v-show="next"
                 @click="getMessageAnswers"
                 class="btn btn-sm btn-outline-success"
                 >Carica Ancora
              </button>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
import AnswerComponent from "../components/Answer.vue";
import MessageActions from "../components/MessageActions.vue";
export default {
    name: "Message",

    props: {
        slug:{
            type: String,
            required: true
        }
    },

    components: {
        AnswerComponent,
        MessageActions

    },

    data() {
        return {
            message: {},
            loadingAnswers: false,
            answers: [],
            userHasAnswered: false,
            showForm: false,
            newAnswerBody: null,
            error: null,
            next:null,
            requestUser:null
        }
    },

    computed: {
        isOwner() {
            return this.message.author === this.requestUser;
        },
        notFound() {
            return this.message["detail"];
        }
    },

    methods: {
        setPageTitle(title) {
            document.title= title;
        },
        setRequestUser() {
            this.requestUser = window.localStorage.getItem("username");
        },
        getMessageData() {
            let endpoint = `/api/messagestext/${this.slug}/`;
            apiService(endpoint)
                .then(data => {
                  this.message = data;
                  this.userHasAnswered = data.user_has_answered;
                  this.setPageTitle(data.content); //funzione per far si che il title sia uguale al contenuto del message
                })
        },
        getMessageAnswers() {
            let endpoint = `/api/messagestext/${this.slug}/answers/`;
            if(this.next) {
               endpoint = this.next;
            }
            this.loadingAnswers = true;
            apiService(endpoint)
                .then(data => {
                    this.answers.push(...data.results);
                    this.loadingAnswers = false;
                    if (data.next) {
                        this.next = data.next;
                    } else {
                      this.next = null;
                    }
                })
        },
        onSubmit() {
          if (this.newAnswerBody) {
              let endpoint = `/api/messagestext/${this.slug}/answer/`;
              apiService(endpoint, "POST", { body: this.newAnswerBody})
                  .then(data => {

                    this.answers.unshift(data);
                  })
              this.newAnswerBody = null;
              this.showForm = false;
              this.userHasAnswered = true;
              if(this.error) {
                 this.error = null;
              }
          } else {
              this.error = "Il campo non può essere vuoto!"
          }
      },
       async deleteAnswer(answer) {
          let endpoint = `/api/answers/${answer.id}/`;
          try{
             await apiService(endpoint, "DELETE");
             //this.answers.splice(this.answers.indexOf(answer), 1);
             this.$delete(this.answers, this.answers.indexOf(answer))
             // this.userHasAnswered = false;
          }
          catch (err) {
             console.log(err);
          }
      }
    },

    created(){
       this.getMessageData();
       this.getMessageAnswers();
       this.setRequestUser();
    }
}
</script>

<style lang="css" scoped>

.container{
  margin-top: 20px;
  margin-bottom: 5px;
}
.answer_added {
  color: green;
  font-weight: bold;
}
.error {
  color: red;
  font-weight: bold;
}
</style>
