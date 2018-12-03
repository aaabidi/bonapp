Rails.application.routes.draw do
  get 'foods/name:string'
  get 'foods/description:text'
  get 'foods/has_many:comments'
  get 'foods/references:halls'
  resources :amenities
  resources :amenities do
    resources :statuses
  end
  
  resources :foods do
    resources :comments
  end

  resources :halls do
    resources :foods
  end

  resources :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
