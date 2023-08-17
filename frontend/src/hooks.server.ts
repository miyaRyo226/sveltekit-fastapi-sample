import { SvelteKitAuth } from "@auth/sveltekit";
import CredentialProvider from "@auth/core/providers/credentials";

export const handle = SvelteKitAuth({
  trustHost:true,
  providers: [CredentialProvider({
    name:"ログイン",
    credentials:{
        username: { label: "ユーザー名", type: "text", placeholder: "ユーザー名" },
        password: {  label: "パスワード", type: "password" }
    },
    async authorize(credentials, request) {
        console.log("通過")
        return Promise.resolve({id:"1",name:"testuser",email:"test@example.com",image:"aaa"}) 
    },
  })],
  
  callbacks: {
    // `jwt()`コールバックは`authorize()`の後に実行されます。
    // `user`に追加したプロパティ`role`と`backendToken`を`token`に設定します。
    jwt({ token, user }) {
      console.log("jwt")
      console.log(token,user)
      if (user) {
        token.name = user.name;
        token.id = user.id;
        token.email = user.email
        token.picture = user.image
      }
      return token;
    },
    // `session()`コールバックは`jwt()`の後に実行されます。
    // `token`に追加したプロパティ`role`と`backendToken`を`session`に設定します。
    session({ session, token }) {
    console.log("tuu")
    console.log("session",session);
      (session.user as {
    name?: string | null | undefined;
    email?: string | null | undefined;
    image?: string | null | undefined;
}).name = token.name;
      return session;
    },
  },
});