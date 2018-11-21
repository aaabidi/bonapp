Rails.application.routes.draw do
  resources :amenities
  resources :foods
  resources :halls
  resources :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
