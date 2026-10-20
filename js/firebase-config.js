// ==========================================================================
// CANNACATALOG 2.0 MAX - CONFIGURACIÓN OFICIAL FIREBASE SDK
// ==========================================================================

const firebaseConfig = {
  apiKey: "AIzaSyB0vceOTI8Yhd1-XXBS4KRdFo0SQo-itzU",
  authDomain: "cannaculture-fb927.firebaseapp.com",
  projectId: "cannaculture-fb927",
  storageBucket: "cannaculture-fb927.firebasestorage.app",
  messagingSenderId: "994926628021",
  appId: "1:994926628021:web:0d41afc6d178f0f82d42fc",
  measurementId: "G-ZHR1FZVQGZ"
};

let auth = null;
let db = null;
let googleProvider = null;

try {
  if (typeof firebase !== 'undefined') {
    if (!firebase.apps || !firebase.apps.length) {
      firebase.initializeApp(firebaseConfig);
    }
    auth = firebase.auth();
    db = firebase.firestore();
    googleProvider = new firebase.auth.GoogleAuthProvider();
    googleProvider.setCustomParameters({ prompt: 'select_account' });
  } else {
    console.warn('⚠️ Firebase SDK no detectado aún en el contexto global.');
  }
} catch (err) {
  console.error('❌ Error inicializando Firebase:', err);
}

// Exportar globalmente para acceso en el bundle y módulos
window.firebaseConfig = firebaseConfig;
window.auth = auth;
window.db = db;
window.googleProvider = googleProvider;
